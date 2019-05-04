#import the flask library
from flask import Flask
#Get the SDK for Alexa 
from flask_ask import Ask, statement, question
#import os module to get environment variable
import os
#import random to get knock knock jokes
import random

app = Flask(__name__)

#Connecting Website to Amazon Alexa
ask = Ask(app,"/game")

#store jokes in here
jokes = {
	"orange" : "Orange you glad I didn't say banana?",
	"boo" : "Why are you crying? It is just a joke.",
	"cargo" : "Car go beep beep, vroom vroom.",
	"hike" : "I didn't know you loved Japanese poetry.",
	"alex" : "Alex plain when you open the door."
}

#AMAZON ALEXA 
@ask.launch
def launch_skill():
	#Return an intrudction 
	welcome_message = "Welcome. Would you like to hear a knock knock joke?"
	return question(welcome_message)

@ask.intent("StartJokeIntent")
def start_joke():
	#Start the joke by saying knock knock.
	beginning_hook = "Okay. Knock Knock."
	return question(beginning_hook)

@ask.intent("WhosThereIntent")
def who_is_there():
	#get the list of hooknames from the jokes dictionary
	joke_list = jokes.keys()
	#randomly select a hook from the list of hooknames
	joke_hook = joke_list[random.randint(0,len(joke_list) - 1)]
	#return that hookname to the user
	return question(joke_hook)

@ask.intent("BlankWhoIntent")
def blank_who(hookname):
	#check to see if the hookname is in the jokes dictionary
	if hookname in jokes.keys():
		#Get the punchline from the jokes dictionary
		punchline = jokes[hookname]
		#return the punchline to the user and ask them if they want to hear another joke.
		return question(punchline + " Would you like to hear another one?")
	return statement("You messed up the joke.")

@ask.intent("NoIntent")
def stop_jokes():
	#create an end message
	conclusion = "Okay. Thank you for your time."
	return statement(conclusion)

@app.route('/')
def index():
	return "Hi mom."

if __name__ == "__main__":
	app.run(debug = True)
