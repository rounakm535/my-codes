from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer

#Create a chatbot instance
chatbot= ChatBot("MyChatBot")

#create a new trainer for the chatbot
trainer= ChatterBotCorpusTrainer(chatbot)

#Train the chatbot using english corpus
trainer.train("chatterbot.corpus.english")

#chatloop 
while True:
  #get user input
  user_input=input("YOU: ")

# Exit the loop if the user enters 'bye'
if user_input.lower() == 'bye':
  "break" 
  # Get the chatbot's response
  bot_response = chatbot.get_response(user_input)

# Print the chatbot's response
print("ChatBot:", bot_response)
"pip install chatterbot"