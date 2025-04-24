# AccelerAI Chatbot

A simple interactive chatbot built with Google's Gemini API that provides helpful responses to user queries.

## Features

- Integrates with Google's Gemini 2.0 Flash model
- Command-line interface for easy interaction
- Maintains conversation history for contextual responses
- Simple to use and extend

## Prerequisites

- Python 3.6+
- Google Generative AI Python SDK
- Google API key for Gemini

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/accelerai-chatbot.git
   cd accelerai-chatbot
   ```

2. Install dependencies:
   ```
   pip install google-generativeai
   ```

3. Set up your API key:
   - Create a `.env` file in the project root directory
   - Add your Gemini API key: `GOOGLE_API_KEY=your_api_key_here`
   - Make sure to add this file to your `.gitignore`

## Usage

Run the chatbot:

```
python main.py
```

Type messages to interact with the bot. Type 'exit' to end the session.

## Security Considerations

- Never commit your API key to version control
- Use environment variables or a secure configuration method
- Consider rate limiting for production use

## License

[Choose an appropriate license for your project]

## Acknowledgements

- Google Generative AI team for the Gemini API