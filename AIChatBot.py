from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import random

# Set the chatbot's name
chatbot_name = "Hellen"

template = f"""
You are a helpful AI named {chatbot_name}. Answer the question below.

Here is the conversation history: {{context}}

Question: {{question}}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Simple list of jokes for the bot to use
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you get when you cross a snowman and a vampire? Frostbite!",
    "Why was the math book sad? Because it had too many problems."
]

# Initialize the context, an empty string or a basic template to store the conversation history.
context = ""

# Function to generate a response with the updated context
def generate_response(chatbot_name, question, previous_context):
    template = f"""
    You are a helpful AI named {chatbot_name}. Answer the question below.

    Here is the conversation history: {previous_context}

    Question: {question}
    Answer:
    """
    # Call your model or function to generate an answer (mocked here as a simple response)
    answer = "This is a generated answer."

    # Update the context with the new question and answer
    updated_context = previous_context + f"\nQuestion: {question}\nAnswer: {answer}\n"

def detect_joke(user_input):
    # Simple keyword detection for jokes
    joke_keywords = ["joke", "funny", "laugh", "humor", "haha", "lol"]
    return any(keyword in user_input.lower() for keyword in joke_keywords)

def recognize_main_user(user_input):
    # Check if the user input matches the "Hey Hellen" phrase
    return user_input.lower() == "hey hellen"

def handle_conversation():
    context = ""
    print(f"Type 'reset' to clear the conversation history or 'exit' to quit.")

    while True:
        user_input = input("> ")

        # Recognize if the user is the main user
        if recognize_main_user(user_input):
            print(f"{chatbot_name}: Welcome Lambros! What are your plans today?")
            continue

        # Check if the user wants to reset the context
        if user_input.lower() == "reset":
            context = ""
            print("Conversation history cleared. How can I assist you now?")
            continue  # Continue to the next iteration of the loop

        # Check if the user wants to exit
        elif user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Detect if the user is telling a joke
        if detect_joke(user_input):
            # Respond with a joke or a humorous comment
            response = random.choice(jokes)
            print(f"{chatbot_name}: Haha! Good one! Here's a joke for you: {response}")
        else:
            # Otherwise, process the input with the model
            result = chain.invoke({"context": context, "question": user_input})
            print(f"{chatbot_name}:", result)

            # Update the context with the latest interaction
            context += f"\nUser: {user_input}\n{chatbot_name}: {result}"

if __name__ == "__main__":
    handle_conversation()

