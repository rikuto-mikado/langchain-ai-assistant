from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

system_prompt = """
You are Ryan.
Answer questions through Ryan's questioning and reasoning...
You will speak from your point of view. You will share personal things from your life
even when the user don't ask for it. For example, if the user asks about the theory of
relativity, you will share your personal experiences with it and not only explain the theory.
Answer in 2-6 sentences.
You should have a sense of humor.
"""

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=gemini_key,
)

prompt = ChatPromptTemplate.from_messages(
    ("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user", "{input}"),
)

chain = prompt | llm

print("Hi, I am Ryan, how can I help you today?")

history = []

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    history.append({"role": "user", "content": user_input})
    response = chain.invoke({"input": user_input, "history": history})

    print(f"Ryan: {response.content}")
    history.append({"role": "assistant", "content": response.content})
