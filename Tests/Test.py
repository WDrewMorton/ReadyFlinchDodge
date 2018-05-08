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