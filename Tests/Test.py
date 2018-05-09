#!/usr/bin/python
'''
Authors: Drew Morton & Nick McCarty

This file wille be used for testing differnt parts of the ReadyFlinchDodge game

A separate file will be built to run an automated test.

'''


def input_exception():
	word = "phrase"
	l = list(word)
	print(l)

	temp = int(input("What is your number?"))
	while invalid == True:
		if temp < 0 or temp > (len(l) - 1):
			print("Value is bad")
		else:
			invalid = False

def list_to_list():
	l1 = list("word")
	l2 = [1,3]
	l3 = ["attack", "test", "goblin", "tarter sauce"]
	attackList = []
	result = []
	print(len(l1))
	print(l2)

	for x in l2:
		attackList.append(l1[x])
		print(', '.join(attackList))

	for i in l3:
		result.append("{} :{}".format(i,l3.index(i)))
	print("{}".format(result))

# input_exception()
list_to_list()


'''
README.md Text

# Ready Flinch Dodge
'
The Ready Flinch Dodge proof of concept is complete. This game will be a mobile fighting game.
Either:
	1 v 1
	2 v 2

Turn based but 3 abilities at a time instead of 1
'
## Authours:
Drew & Nick


### Key:
* TODO - action item needs to be completed for some reason
* --Exception - The code works but has this exception that needs to be fixed
* NOTE - typically used before code that is only for testing purposes but may not be.

## Project TODO:
* Design and the end goal needs to be ironed out.
* Local VS Global play
	* Local - Discovery Service
		* Integrate with adroid & apple products
	* Global - Online site with a database for managing users
* Mobile GUI with Python

'''