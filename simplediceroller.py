#Rishabh Shah
#2016
#Simple Dice Roller

#Imports
import random
import sys

#Global Variables
diceValues = list(xrange(1,7))

#Defining functions
def diceRoller():
	diceValue1 = str(random.choice(diceValues))
	diceValue2 = str(random.choice(diceValues))
	totalValue = str(int(diceValue2)+int(diceValue1))
	print "Dice 1 is " + diceValue1 + "."
	print "Dice 2 is " + diceValue2 + "."
	print "Total value of dice is " + totalValue + "."

def playAnotherTime():
	while True:
		playAgain = raw_input("Would you like to roll again? (yes/no): ").lower()
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

#Running the functions
while True:
	diceRoller()
	playAnotherTime()