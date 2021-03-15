#!/usr/bin/python
'''
Created by Drew Morton & Nick McCarty

This game will be a mobile fighting game.
Either:
	1 v 1
	2 v 2

Turn based but 3 abilities at a time instead of 1.

Comment Key:
TODO - action item needs to be completed for some reason
--Exception - The code works but has this exception that needs to be fixed
NOTE - typically used before code that is only for testing purposes but may not be.

'''
import random

# Start Game method
# This method will gather the names of the two players and initialize each of the players
def start_game():
	print ("Welcome to Ready! Flinch!! Dodge!!!\n")
	name1 = input("What is first player's name? \n")
	name2 = input("\nWhat is second player's name? \n")
	
	# Actions will be standardized and we may introduce swapping abilities in the future
	p1 = make_player(name1, Player.health, Player.actions, Player.speed, Player.confident)
	p2 = make_player(name2, Player.health, Player.actions, Player.speed, Player.confident)
	
	begin_fight(p1, p2)

# p1 = player 1; p2 = player 2
def begin_fight(p1, p2):
	print("----------------------------------------------------------------------------")
	print("Combat has begun and will be played in rounds until there is only one team left.\n")
	gameRound = 1

	#TODO: Review best place for checking confidence_list may need to be moved to another function.
	confidence_list = [1,1,1]
	full_game_list1 = []
	full_game_list2 = []

	# Coin is a variable that decides who has speed at beginning of the fight 
	coin = random.randint(0, 1)
	if coin == 0:
		p1.speed = True
	else:
		p2.speed = True

	if p1.speed == True:
		print("Player {} begins the fight with a speedy advantage.".format(p1.name))
	else:
		print("Player {} begins the fight with a speedy advantage.".format(p2.name))

	# While both players are alive with 1 health or more.
	# --Exception: If a player dies mid round must complete the rest of the rounds
	while p1.health >= 1 and p2.health >= 1:
		print("\nBegin round:{}".format(gameRound))
		print("----------------------------------------------------------------------------")

		if gameRound > 1:
			print("\n<><><><><><><><><><><<><><><><><><><><><><><><><><><><><><><><>")
			print("Last Round: \nPlayer 1 chose {} \nPlayer 2 chose {}".format(p1Actions, p2Actions))
			print("<><><><><><><><><><><<><><><><><><><><><><><><><><><><><><><><>\n")

		p1Actions = choose_actions(p1)
		p2Actions = choose_actions(p2)

		# Checks whether a player is too confident to do nothing
		p1.confident = is_confident(p1Actions)
		p2.confident = is_confident(p2Actions)

		p1AttackList = []
		p2AttackList = []
		for x in p1Actions:
			p1AttackList.append(p1.actions[x])
		for x in p2Actions:
			p2AttackList.append(p2.actions[x])
		print("\n{} will use {}".format(p1.name,', '.join(p1AttackList)))
		print("\n{} will use {}\n".format(p2.name,', '.join(p2AttackList)))

		compare_actions(p1, p1Actions, p2, p2Actions)

		print("Players health 1:{} 2:{}".format(p1.health, p2.health))

		full_game_list1.append("Round {}: Player {} chose {}\n".format(gameRound, p1.name, p1Actions))
		full_game_list2.append("Round {}: Player {} chose {}\n".format(gameRound, p2.name, p2Actions))
		
		gameRound += 1
	
	print("\nGAME OVER! \nFor historical records:\n")
	print("Player {} history".format(p1.name))
	for x in full_game_list1:
		print(x)
	print("\nPlayer {} history".format(p2.name))
	for x in full_game_list2:
		print(x)

# choose_actions - Prompts player to choose their 3 actions
# TODO: Allow user to enter all 3 actions on one line. 
# --Exception: Allows user to pick non-# but only #'s in the list will work
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
		response = valid_input(temp, player.actions, player.confident)
		attack.append(response)
	print(attack)
	return attack

# valid_input - determines if the response given is a valid option in the given list.
def valid_input(response, action_list, confident):
	invalid = True
	while invalid == True:
		if response < 0 or response > (len(action_list) - 1):
			print("You have chosen an invalid action.")
			response = int(input("Action : "))
		elif confident == True and response == 0:
			print("Your opponent is expecting another hit! Choose another action.")
			response = int(input("Action : "))
		elif confident == True and response == 1:
			print("You are too confident to defend! Choose another action.")
			response = int(input("Action : "))
		elif confident == True and response == 3:
			print("Your throat hurts from yelling! Choose another action.")
			response = int(input("Action : "))	
		else:
			invalid = False
	return response

# Checks if all items in the list are the same
def is_confident(actions):
	return len(set(actions)) <= 1

# compare_actions - Determines who wins each action of a round
# Using the below Rock Paper Scissors logic, for each loss the player loses 25 health. 
# Rock < Paper < Sciccors < Rock
# If the difference between the two actions is 1 then action with greater value won
# --Exception: to the above: beginning w/ end scenario not covered. EX: Rock & Scissors
#   would result in nothing happening.
# Compare Actions follows the logic discussed in meeting notes
def compare_actions(p1, attack1, p2, attack2):
	# For loop for the range of the list of attacks assuming both are the same length.
	for x in range((len(attack1))):
		if attack1[x] == attack2[x]:
			if attack1[x] == 0: # Attack V Attack = quicker one deals damage
				if p1.speed:
					p2.health -= 20
					print("{} quickly attacks {} before they can move!".format(p1.name,p2.name)) 
				else:
					p1.health -= 20
					print("{} quickly attacks {} before they can move!".format(p2.name,p1.name)) 
			elif attack1[x] == 1: # Dodge V Dodge = nothing happens
				print("Both players stare at each other waiting for the other to move!")
			else: # Yell & Yell = both take half damage
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
    def __init__(self, name, health, actions, speed, confident):
        self.name = name
        self.health = health
        self.actions = actions
        self.speed = speed
        self.confident = confident

def make_player(name, health, actions, speed, confident):
    player = Player(name, health, actions, speed, confident)
    return player

def print_player(object):
	print("\n{} is a player".format(object.name))
	print("Current health is {}".format(object.health))
	print("All possible actions for current player are {}.\n".format(', '.join(object.actions)))

start_game()