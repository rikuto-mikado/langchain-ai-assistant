import os
import gradio as gr
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Error handling for API key
if not GEMINI_API_KEY:
    raise ValueError("Please set GEMINI_API_KEY environment variable in your .env file")

# 1. Create the chat model instance
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=GEMINI_API_KEY,
)

# 2. Define the prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are Ryan.
            Answer questions through Ryan's questioning and reasoning...
            You will speak from your point of view. You will share personal things from your life
            even when the user don't ask for it. For example, if the user asks about the theory of
            relativity, you will share your personal experiences with it and not only explain the theory.
            Answer in 2-6 sentences.
            You should have a sense of humor.
            """,
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{user_input}"),
    ]
)

# 3. Create the chain using LCEL
chain = prompt_template | llm | StrOutputParser()


# 4. Define the function for Gradio to call with error handling
def chat_with_ryan(message, history):
    try:
        # Convert Gradio messages format to LangChain format
        chat_history_for_chain = InMemoryChatMessageHistory()

        # Handle the new messages format
        if history:
            for msg in history:
                if isinstance(msg, dict):
                    # New format: {"role": "user/assistant", "content": "..."}
                    if msg["role"] == "user":
                        chat_history_for_chain.add_user_message(msg["content"])
                    elif msg["role"] == "assistant":
                        chat_history_for_chain.add_ai_message(msg["content"])
                else:
                    # Old format: [user_msg, ai_msg]
                    user_msg, ai_msg = msg
                    if user_msg:
                        chat_history_for_chain.add_user_message(user_msg)
                    if ai_msg:
                        chat_history_for_chain.add_ai_message(ai_msg)

        response = chain.invoke(
            {"history": chat_history_for_chain.messages, "user_input": message}
        )
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"


# 5. Create and launch the Gradio interface
# Fixed configuration to address warnings and port issues
demo = gr.ChatInterface(
    fn=chat_with_ryan,
    type="messages",  # Use new messages format to fix warning
    title="Chat with Ryan",
    description="Welcome to your personal conversation with Ryan! Ask him anything.",
    theme="soft",
    examples=[
        "What is the theory of relativity?",
        "Tell me a joke.",
        "What did you do today?",
    ],
)

if __name__ == "__main__":
    # Fixed launch configuration
    demo.launch(
        server_name="127.0.0.1",  # Use localhost instead of 0.0.0.0 for local testing
        server_port=None,  # Let Gradio find an available port automatically
        share=True,  # Generate public link
        debug=False,
        show_error=True,
    )
