import os
from groq import Groq
import logging

logging.basicConfig(
    filename=".logs",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Initialize the Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def create_chat_completion(
    prompt: str, model: str = "llama3-8b-8192", max_tokens: int = 100
):
    """Function to create a chat completion

    Args:
        prompt (str): User Input
        model (str): Choose a model to use. Defaults to "llama3-8b-8192".
        max_tokens (int): Max token for the model

    Returns:
        str: Output from LLM Model
    """
    try:
        logging.info("LLM API hit, Chat Completion Started")
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant specializing in creating engaging social media threads. write as first person and keep it under 500 character",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            model=model,
            max_tokens=max_tokens,
        )
        logging.info("Completion Complete")
        return response.choices[0].message.content
    except Exception as e:
        logging.error("Error in chat completion: %s", e)
        return f"Error: {e}"
