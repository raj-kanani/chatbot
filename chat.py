# python -m pip install chatterbot==1.0.4 pytz
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot
chatbot = ChatBot('CustomBot')

# Read your dataset from a text file
dataset_file = "chatbot_dataset.txt"

# Assuming your dataset is already in the format [(question1, answer1), (question2, answer2), ...]
with open(dataset_file, 'r', encoding='utf-8') as file:
    dataset = [line.strip().split('\t') for line in file]

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Train the chatbot on your custom dataset
trainer.train(dataset)

# Simple conversation loop
print("Hello! I'm CustomBot. Ask me anything or type 'bye' to exit.")

while True:
    user_input = input("You: ")

    # Exit the loop if the user says 'bye'
    if user_input.lower() == 'bye':
        print("CustomBot: Goodbye!")
        break

    # Get the chatbot's response
    response = chatbot.get_response(user_input)

    print(f"CustomBot: {response}")
