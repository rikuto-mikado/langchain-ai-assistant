# LangChain Gemini Chatbot

A simple, web-based chatbot powered by Google's Gemini model through the LangChain framework. This interactive application lets you have a conversation with an AI persona named "Ryan" via a Gradio interface.

## Features

-   **Interactive Web Chat:** Engage in a back-and-forth conversation through a user-friendly web interface.
-   **Persona-driven:** The AI responds as "Ryan," a character with a sense of humor and a tendency to share personal anecdotes, based on a system prompt.
-   **Conversation History:** The chatbot remembers previous turns in the conversation to maintain context.
-   **Powered by LangChain and Gemini:** Utilizes `langchain-google-genai` to connect to the Gemini API.
-   **Easy to Use:** Built with Gradio for a clean, simple user experience.

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

This will launch a Gradio web server. You can interact with the chatbot by opening the local URL (usually `http://127.0.0.1:7860`) provided in your terminal in a web browser. The application will also generate a public link for sharing.