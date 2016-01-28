#Rishabh Shah
#2016
#Craps

#imports
import random
import sys

#global variables
diceValues = list(xrange(1,7))

#Defining functions
def rollDice():
	diceValue1 = str(random.choice(diceValues))
	diceValue2 = str(random.choice(diceValues))
	totalValue = str(int(diceValue2)+int(diceValue1))
	print "Dice 1 is " + diceValue1 + "."
	print "Dice 2 is " + diceValue2 + "."
	print "Total value of dice is " + totalValue + "."

def playAnotherTime():
	while True:
		playAgain = raw_input("Would you like to play again? (yes/no): ").lower()
		if playAgain == "no" or playAgain == "n":
			print ""
			print "Goodbye"
			sys.exit()
		if playAgain == "yes" or playAgain == "y":
			print ""
			return
		if playAgain != "yes" or playAgain != "y" or playAgain != "no" or playAgain != "n":
			print ""
			print "You entered something that does not compute. Please try again"

def play():
	while True:
		play = raw_input("Would you like to play? (yes/no): ").lower()
		if play == "no" or playAgain == "n":
			print ""
			print "Goodbye"
			sys.exit()
		if play == "yes" or playAgain == "y":
			print ""
			return
		if play != "yes" or playAgain != "y" or playAgain != "no" or playAgain != "n":
			print ""
			print "You entered something that does not compute. Please try again"

def main():
	print "Welcome to Rishabh Shah's craps game!"
	play()
	rollDice()
	if int(totalValue) == 7 or int(totalValue) == 11:
		print "You win!"
		playAnotherTime()
	if int(totalValue) == 2 or int(totalValue) == 3 or int(totalValue) == 12:
		print "You lose!"
		playAnotherTime
	if int(totalValue) != 7 or int(totalValue) != 11 or int(totalValue) != 2 or int(totalValue) != 3 or int(totalValue) != 12:
		point = totalValue
		print point + " is the point!"
		rollDice()
		if point == totalValue:
			print "You win!"
			playAnotherTime
		elif int(point) == 7 or int(point) == 11:
			print "You lose!"
			playAnotherTime
		elif int(point) != int(totalValue) or int(point) != 7 or int(point) != 11:
			rollDice()