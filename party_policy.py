import random

def canAnswer(query):
	canAnswer = random.random() < 0.3
	if(canAnswer):
		print("I can answer the question")
	else:
		print("I can't answer the question")
	return canAnswer

def getBody(query):
	answer = random.random() < 0.5
	print("Random answer:", answer)
	return [answer]

def trustSomeone(query):
	print("But I trust someone to answer this")
	return True