from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

# 1. Create the chat model instance
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=gemini_key,
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

# 3. Create the chain using LCEL, now with the output parser
chain = prompt_template | llm | StrOutputParser()

# 4. Main application loop
print("Hi, I am Ryan, how can I help you today?")

# Use a more robust history object
chat_history = InMemoryChatMessageHistory()

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # 5. Use the new chain for invocation
    response = chain.invoke(
        {"history": chat_history.messages, "user_input": user_input}
    )

    # The response is now a simple string, thanks to StrOutputParser
    print(f"Ryan: {response}")

    # Add user input and AI response to history
    chat_history.add_user_message(user_input)
    chat_history.add_ai_message(response)
