# LangChain Gemini Chatbot

A simple, command-line chatbot powered by Google's Gemini model through the LangChain framework. This interactive script lets you have a conversation with an AI persona named "Ryan".

## Features

-   **Interactive Chat:** Engage in a back-and-forth conversation directly in your terminal.
-   **Persona-driven:** The AI responds as "Ryan," a character with a sense of humor and a tendency to share personal anecdotes, based on a system prompt.
-   **Conversation History:** The chatbot remembers previous turns in the conversation to maintain context.
-   **Powered by LangChain and Gemini:** Utilizes `langchain-google-genai` to connect to the Gemini API.

## Requirements

-   Python 3.7+
-   An API key for the Gemini API.

## Setup and Installation

1.  **Clone the repository (optional):**
    If you have cloned this project, you can proceed to the next steps.

2.  **Install dependencies:**
    Install the required packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your API Key:**
    Create a file named `.env` in the root of the project directory and add your Gemini API key to it:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
    Replace `"YOUR_API_KEY_HERE"` with your actual key.

## Usage

Once the setup is complete, run the chatbot with the following command:

```bash
python app.py
```

You can then start chatting with Ryan. Type `exit` to end the conversation.
