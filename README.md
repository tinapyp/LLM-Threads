# LLM-Threads
This project is based on my idea: `how if I can make an LLM as a writer in my Threads to make me famous 🤣`

## Introduction
LLM-Threads leverages the power of large language models (LLMs) to automate the creation and posting of engaging social media content, specifically designed for daily tweets about Python, data science, SQL, and machine learning. The goal is to gain 10k followers in 100 days by consistently sharing valuable and interesting content.

## Features
- Automated generation of daily tweets based on specific prompts for each day of the week.
- Customizable character limit for tweets to ensure they fit within platform constraints.
- Logging of activities and errors for easy monitoring and debugging.
- Secure authentication with environment variables.
- Integration with the ThreadsAPI for seamless content posting.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/LLM-Threads.git
    cd LLM-Threads
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables. Create a `.env` file in the project root and add the following:
    ```bash
    USERNAME=your_threads_username
    PASSWORD=your_threads_password
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage
To run the script and start generating and posting tweets, simply execute:
```bash
python main.py
```

## Configuration
- **Logging**: Logs are saved in the `.log` file in the project root directory.
- **Daily Prompts**: You can customize the daily prompts by editing the `prompts` dictionary in `main.py`.
- **Character Limit**: The character limit for tweets is set to 500 by default. This can be adjusted in the `truncate_to_character_limit` function.

## Logging
All activities and errors are logged to a file named `.log`. This includes information on API calls, content generation, and publishing statuses.