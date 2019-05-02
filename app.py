#import the flask library
from flask import Flask, render_template
#Get the SDK for Alexa 
from flask_ask import Ask, statement, question, session
#import os module to get environment variable
import os
#import random to generate questions
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
	welcome_message = "Welcome. Would you like to hear a knock knock joke?"
	return question(welcome_message)

@ask.intent("StartJokeIntent")
def start_joke():
	beginning_hook = "Okay. Knock Knock."
	return question(beginning_hook)

@ask.intent("WhosThereIntent")
def who_is_there():
	joke_list = jokes.keys()
	joke_hook = joke_list[random.randint(0,len(joke_list))]
	return question(joke_hook)

@ask.intent("BlankWhoIntent")
def blank_who(hookname):
	if hookname in jokes.keys():
		punch_line = jokes[hookname]
		return statement(punch_line)
	return statement("You messed up the joke.")

@app.route('/')
def index():
	return "Hi mom."

if __name__ == "__main__":
	app.run(debug = True)
