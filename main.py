import os
import google.generativeai as genai

# Configure the API key!
GOOGLE_API_KEY = "AIzaSyCdVf2DV_7wjrQeMQDLJ6jazX3hCumQ9s0"  # Replace with your Gemini API key!
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini model with a system instruction!
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction="Reply as a helpful assistant. "
    "You can answer questions, provide explanations, and assist with various tasks. "
)

# Start a chat session!
chat = model.start_chat(history=[])

print("Welcome to the AccelerAI Chatbot! Type 'exit' to quit.")
while True:
    # Get user input!
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Thanks for using AccelerAI, Goodbye!")
        break

    # Send message to Gemini and get response!
    response = chat.send_message(user_input)
    print("Bot:", response.text)