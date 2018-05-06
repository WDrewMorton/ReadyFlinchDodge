#!/usr/bin/python
'''
Created by Drew Morton
Last Editted: 05/05/18

This game will be a mobile fighting game.
Either:
	1 v 1
	2 v 2

Turn based but 3 abilities at a time instead of 1

Key:
TODO - action item needs to be completed for some reason
--Exception - The code works but has this exception that needs to be fixed
NOTE - typically used before code that is only for testing purposes but may not be.

'''
import random

# Start Game method will 
def start_game():
	name1 = input("What is first player's name? \n")
#	print("\n")
	name2 = input("\nWhat is second player's name? \n")
	health = 100
	# tickle/melee, flinch/dodge, backhand/counter buff, scream/debuff
	actions1 = ["tickle", "flinch", "backhand", "scream"]
	actions2 = ["flick", "blink", "shrug", "flex"]
	
	p1 = make_player(name1, health, actions1)
	p2 = make_player(name2, health, actions2)
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
	
	# While both players are alive
	# --Exception:
	while p1.health > 0 and p1.health > 0:
		print("Begin round:{}".format(gameRound))
		print("--------------------------------------")

		# TODO: make separate function to assign actions per round
		p1Actions = choose_actions(p1)
		print("{}\n".format(p1Actions))
		p2Actions = choose_actions(p2)
		print("{}".format(p2Actions))
		compare_actions(p1, p1Actions, p2, p2Actions)

		print("Players health 1:{} 2:{}".format(p1.health, p2.health))
		gameRound += 1


# choose_actions - Prompts player to choose their 3 actions
# TODO: Allow user to click a button, enter string, and/or all 3 actions on one line. 
# --Exception: Allows user to pick outside of action range 
def choose_actions(player):
	print("{} choose 3 of your listed actions: {}\n".format(player.name, ', '.join(player.actions)))
	print("Select your action via the position. First postition is 0.")
	'''
	while a1 < 0 and a1 > len(player.actions) - 1:
		a1 = int(input("Action 1: "))
		if a1 < 0 or a1 > len(player.actions) - 1:
			print("You have entered an invalid answer")
	'''
	a1 = int(input("Action 1: "))
	a2 = int(input("Action 2: "))
	a3 = int(input("Action 3: "))
	attack = [a1, a2, a3]
	return attack


# compare_actions - Determines who wins each action of a round
# Using the below Rock Paper Scissors logic, for each loss the player loses 25 health. 
# Rock < Paper < Sciccors < Rock
# If the difference between the two actions is 1 then action with greater value won
# --Exception: to the above: beginning w/ end scenario not covered. EX: Rock & Scissors
#   would result in nothing happening.
def compare_actions(p1, attack1, p2, attack2):
	for x in range(3):
		if attack1[x] > attack2[x]:
			r = attack1[x] - attack2[x] 
			if r == 1:
				print("Player 1 damaged Player 2")
				p2.health -= 25
				#Test
				print("Player 2 health: {}".format(p2.health))
			else:
				print("Woosh, nothing happens")
		elif attack1[x] < attack2[x]:
			r = attack2[x] - attack1[x] 
			if r == 1:
				print("Player 2 damaged Player 1")
				p1.health -= 25
				print("Player 1 health: {}".format(p1.health))
			else:
				print("Phew, nothing happens")
		else:
			# Both values are the same
			print("Draw")

# Player class
# Unsure if naming convention is correct. I think it needs an underscore in front of it.
class Player(object):
    name = ""
    health = 0
    # List to hold all possible actions for the player
    actions = []

    # Initializer 
    def __init__(self, name, health, actions):
        self.name = name
        self.health = health
        self.actions = actions

def make_player(name, health, actions):
    player = Player(name, health, actions)
    return player

def print_player(object):
	print("\n{} is a player".format(object.name))
	print("Current health is {}".format(object.health))
	print("All possible actions for current player are {}.\n".format(', '.join(object.actions)))

print ("Welcome to Ready! Flinch!! Dodge!!!\n")

start_game()