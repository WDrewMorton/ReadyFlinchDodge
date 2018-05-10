#!/usr/bin/python
'''
Created by Drew Morton & Nick McCarty
Last Editted: 05/07/18

This game will be a mobile fighting game.
Either:
	1 v 1
	2 v 2

Turn based but 3 abilities at a time instead of 1

Comment Key:
TODO - action item needs to be completed for some reason
--Exception - The code works but has this exception that needs to be fixed
NOTE - typically used before code that is only for testing purposes but may not be.

'''
import random

# Start Game method 
def start_game():
	name1 = input("What is first player's name? \n")
	name2 = input("\nWhat is second player's name? \n")
	health = 100

	
	# Actions will be standardized and we may introduce swapping abilities in the future
	actions = ["Attack", "Dodge", "Yell"]

	p1 = make_player(name1, health, actions, Player.speed)
	p2 = make_player(name2, health, actions, Player.speed)
	
	print("\n########################################")
	print_player(p1)
	print("########################################")
	print_player(p2)
	print("########################################\n")
	begin_fight(p1, p2)


# p1 = player 1; p2 = player 2
def begin_fight(p1, p2):
	print("Combat has begun and will be played in rounds until there is only one team left.")
	gameRound = 1

	#TODO: Review best place for checking confidence_list may need to be moved to another function.
	#confidence_list = [1,1,1]
	#print(confidence_list)

	# While both players are alive with 1 health or more.
	# --Exception: If a player dies mid round
	while p1.health >= 1 and p2.health >= 1:
		print("Begin round:{}".format(gameRound))
		print("--------------------------------------")

		# TODO: COMPLETE make separate function to assign actions per round
		p1Actions = choose_actions(p1)
		p2Actions = choose_actions(p2)

		p1AttackList = []
		p2AttackList = []
		for x in p1Actions:
			p1AttackList.append(p1.actions[x])
		for x in p2Actions:
			p2AttackList.append(p2.actions[x])
		print("\n{} will use {}".format(p1.name,', '.join(p1AttackList)))
		print("\n{} will use {}\n".format(p2.name,', '.join(p2AttackList)))


		# HARDCODE: Set P1 to have speed in the very beginning
		p1.speed = True

		compare_actions2(p1, p1Actions, p2, p2Actions)

		print("Players health 1:{} 2:{}".format(p1.health, p2.health))
		
		p1.confident = False
		p2.confident = False

		gameRound += 1


# choose_actions - Prompts player to choose their 3 actions
# TODO: Allow user to click a button, enter string, and/or all 3 actions on one line. 
# --Exception: Allows user to pick outside of action range 
#def choose_actions(player, confident):
def choose_actions(player):

	# Re-format action list in format ACTION:EXPECTED INPUT
	formtActionList = []
	for i in player.actions:
		formtActionList.append("{}|{}".format(i,player.actions.index(i)))

	print("{} choose 3 of your listed actions: {}\n".format(player.name, ', '.join(formtActionList)))
	print("Select your action via the position. First postition is 0.")

	# Choose your attacks via # input & store in list
	attack = []
	for x in range(len(player.actions)):
		temp = int(input("Action : "))
		response = valid_input(temp, player.actions)
		attack.append(response)
	print(attack)

	return attack

# valid_input - determines if the response given is a valid option in the given list.
def valid_input(response, l):
	invalid = True
	while invalid == True:
		if response < 0 or response > (len(l) - 1):
			print("You have chosen an invalid action.")
			response = int(input("Action : "))
		else:
			invalid = False
	return response

# compare_actions - Determines who wins each action of a round
# Using the below Rock Paper Scissors logic, for each loss the player loses 25 health. 
# Rock < Paper < Sciccors < Rock
# If the difference between the two actions is 1 then action with greater value won
# --Exception: to the above: beginning w/ end scenario not covered. EX: Rock & Scissors
#   would result in nothing happening.
# Compare Actions 2 follows the logic discussed in meeting notes
def compare_actions2(p1, attack1, p2, attack2):
	# For loop for the range of the list of attacks assuming both are the same length.
	for x in range((len(attack1))):
		if attack1[x] == attack2[x]:
			if attack1[x] == 0: # Attack V Attack
				if p1.speed:
					p2.health -= 20
					print("{} quickly attacks {} before they can move!".format(p1.name,p2.name)) 
				else:
					p1.health -= 20
					print("{} quickly attacks {} before they can move!".format(p1.name,p2.name)) 
			elif attack1[x] == 1: # Dodge V Dodge
				print("Both players stare at each other waiting for the other to move!")
			else: # Yell & Yell
				# both take half damage
				print("Both players yell and hurt one another's ears!")
				p1.health -= 10 
				p2.health -= 10 
		elif abs(int(attack1[x]) - int(attack2[x])) == (len(p1.actions) - 1): # Attack V Yell
			if attack1[x] == 0:
				p2.health -= 20
				print("{} attacks yelling {} in the mouth!".format(p1.name,p2.name)) 
			else:
				p1.health -= 20
				print("{} attacks yelling {} in the mouth!".format(p2.name,p1.name)) 
		# All other attack options have ben checked so whichever player chose attack will win.
		elif (attack1[x] == 0) or (attack2[x] == 0): # Attack V Dodge
			if attack1[x] == 0:
				p1.speed = False
				p2.speed = True
				print("{} has dodged {}'s attack!".format(p2.name,p1.name))
			else:
				p1.speed = True
				p2.speed = False
				print("{} has dodged {}'s attack!".format(p1.name,p2.name))
		else: # Dodge V Yell
			if attack1[x] == 2:
				p2.health -= 20
				print("{} yells at staring {} hurting their ears!".format(p1.name,p2.name)) 
			else:
				p1.health -= 20
				print("{} yells at staring {} hurting their ears!".format(p2.name,p1.name)) 


# Player class
# Unsure if naming convention is correct. I think it needs an underscore in front of it.
class Player(object):
    name = ""
    health = 100
    # List to hold all possible actions for the player
    actions = ["Attack", "Dodge", "Yell"]
    speed = False
    confident = False

    # Initializer 
    def __init__(self, name, health, actions, speed):
        self.name = name
        self.health = health
        self.actions = actions
        self.speed = speed

def make_player(name, health, actions, speed):
    player = Player(name, health, actions, speed)
    return player

def print_player(object):
	print("\n{} is a player".format(object.name))
	print("Current health is {}".format(object.health))
	print("All possible actions for current player are {}.\n".format(', '.join(object.actions)))
	print("Does the player have speed boost? {} ".format(object.speed))

print ("Welcome to Ready! Flinch!! Dodge!!!\n")

start_game()