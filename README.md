# Mini Prompt System
 
### Demo video
 -  https://drive.google.com/file/d/1Mf5Dh3nT25yHUCnHpQply5KnK_0tWe8x/view?usp=sharing


## Overview
Mini Prompt System is a Python-based command-line application that interacts with the OpenAI API to provide conversational responses to user queries. It uses Jinja2 templates for prompt rendering, maintains a conversation history, and supports streaming responses for an interactive experience. The application is designed to be lightweight and extensible, with a focus on clean code structure and user-friendly output using the rich library for formatting. To enhance security, the system implements prompt injection safeguards to prevent users from inserting malicious or unauthorized content into prompts, ensuring safe and controlled interactions.

## Features
- **Conversational Memory**: Stores up to 10 recent question-response pairs to maintain context.
- **Template-Driven Prompts**: Uses Jinja2 templates (`prompt.txt`) for flexible and customizable prompt creation.
- **Streaming Responses**: Supports real-time streaming of OpenAI API responses with a configurable delay.
- **Rich Console Output**: Displays formatted output with timestamps and markdown support using the `rich` library.
- **Environment Configuration**: Loads API keys securely from a `.env` file.
- **Error Handling**: Gracefully handles missing API keys, invalid templates, and API errors.
- **Prompt Injection Security** : Implements safeguards to detect and prevent prompt injections, ensuring users cannot insert   malicious or unauthorized content that could compromise the system's behavior or security.
- **User Intent Recognition in prompt** : Captures the intent of user input to classify whether it's a development-related task (e.g., creating a website, app, or script) or a general question.
If the intent is development-focused, the system provides structured guidance, including step-by-step instructions or code generation.
If the intent is a general inquiry, it returns a concise and informative response.

## Prerequisites
- Python 3.8 or higher
- An OpenAI API key (set in a `.env` file as `OPENAI_API_KEY`)
- Required Python packages (listed in `requirements.txt`)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Divyatec-git/Mini-Prompt-System.git
   cd Mini-Prompt-System
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**:
   - Create a `.env` file in the project root.
   - Add your OpenAI API key:
     ```plaintext
     OPENAI_API_KEY=your-api-key-here
     ```

5. **Create Template Directory**:
   - Create a folder named `templete` in the project root.
   - Add a file named `prompt.txt` in the `templete` folder with your desired prompt structure. Example:
     ```plaintext
     You are a helpful assistant. Answer the following question clearly and concisely: {{ question }}
     ```

## Usage
1. Run the application:
   ```bash
   python main.py
   ```

2. Follow the prompts:
   - Enter a question (e.g., "What is Python?" or "Create a weather app guide").
   - Type `exit` to quit the application.
   - The system will display streaming responses, conversation history, and a clarification prompt after each response.

3. Example interaction:
   ```
   === Mini Prompt System ===
   Started at 11:50 AM IST, Jun 27, 2025
   Ask a question (e.g., 'What is Python?' or 'Create a weather app guide')
   Type 'exit' to end the chat.
   Ask Question: What is Python?
   ```

## Project Structure
```
mini-prompt-system/
├── main.py               # Main application script
├── templete/            # Directory for Jinja2 templates
│   └── prompt.txt         # Prompt template file
├── .env                 # Environment file for API keys (not tracked)
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Dependencies
Install the required packages using:
```bash
pip install openai python-dotenv jinja2 rich
```

## Notes
- Ensure the `templete` directory and `prompt.txt` file exist before running the application.
- The application uses the `gpt-4o` model by default. Modify the `call_openai` function in `main.py` to use a different model if needed.
- Streaming responses include a 0.1-second delay for readability, which can be adjusted via the `stream_delay` parameter.

## Troubleshooting
- **Missing API Key**: Ensure `OPENAI_API_KEY` is set in the `.env` file.
- **Template Not Found**: Verify the `templete` directory and `prompt.txt` file exist.
- **API Errors**: Check your internet connection and OpenAI API status.

