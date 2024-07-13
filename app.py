import os
import logging
from datetime import datetime
from src.model import create_chat_completion
from threadspy import ThreadsAPI
from dotenv import load_dotenv
from src.utils import truncate_to_character_limit, extract_after_result

logging.basicConfig(
    filename=".log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

load_dotenv()

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

# Ensure credentials are available
if not USERNAME or not PASSWORD:
    logging.error("USERNAME or PASSWORD environment variables not set.")
    raise ValueError("USERNAME or PASSWORD environment variables not set.")

today = datetime.now().strftime("%A")

# Daily prompts
prompts = {
    "Monday": "Create a single tweet about a quick Python tip that enhances productivity. Keep it under 500 characters.",
    "Tuesday": "Create a single tweet explaining a key data science concept. Keep it under 500 characters.",
    "Wednesday": "Create a single tweet demonstrating a useful SQL query. Keep it under 500 characters.",
    "Thursday": "Create a single tweet describing a machine learning algorithm and its application. Keep it under 500 characters.",
    "Friday": "Create a single tweet highlighting a data science or machine learning case in real word from big Company dont always netflix. Keep it under 500 characters.",
    "Saturday": "Create a single tweet sharing a quick tech tip. Keep it under 500 characters.",
    "Sunday": "Create a single tweet chilling about tech topics and inviting a Q&A. Keep it under 500 characters.",
}

# Get the corresponding prompt for the day
prompt = prompts.get(
    today,
    "Create a single tweet sharing a quick tech tip. Keep it under 500 characters.",
)


# Function to generate post
def generate_post(prompt):
    try:
        logging.info("Generating chat completion for prompt: %s", prompt)
        response = create_chat_completion(prompt)
        truncated_response = truncate_to_character_limit(response, limit=500)
        final_prompt = f"Make this into a single concise tweet about data science and AI: {truncated_response}. Return in this format 'result:<TWEET>'"
        tweet_response = create_chat_completion(final_prompt)
        tweet = extract_after_result(tweet_response)
        logging.info("Post generated successfully.")
        return tweet
    except Exception as e:
        logging.error("Error generating tweet: %s", e)
        raise


# Generate the post
post = generate_post(prompt)

# Initialize and authenticate with the Threads API
try:
    logging.info("Initializing ThreadsAPI")
    api = ThreadsAPI(username=USERNAME, password=PASSWORD)
    logging.info("Authenticated with ThreadsAPI")
except Exception as e:
    logging.error("Error initializing ThreadsAPI: %s", e)
    raise

# Publish the generated post
try:
    logging.info("Publishing to Threads")
    posted = api.publish(caption=post)
    if posted:
        logging.info("Post published successfully.")
    else:
        logging.error("Error publishing tweet: Publishing content failed.")
except Exception as e:
    logging.error("Error publishing post: %s", e)
    raise
