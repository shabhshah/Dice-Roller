#Rishabh Shah
#2016
#Complex Dice Roller

#Imports
import random
import sys

#Defining Functions
def rollDice():
	while True:
		diceSides = raw_input("How many sides per die?: ")
		try:
			int(diceSides) + 1
		except:
			print ""
			print "You entered something that does not compute. Please try again."
		else:
			break
	while True:
		numberOfDice = raw_input("How many dice to roll?: ")
		try:
			int(numberOfDice) + 1
		except:
			print ""
			print "You entered something that does not compute. Please try again."
		else:
			break
	allValues = []
	diceNumber = 1
	possibleDiceValues = list(xrange(1, (int(diceSides)+1)))
	print ""
	for i in xrange(0, (int(numberOfDice))):
		value = random.choice(possibleDiceValues)
		print "Dice Number " + str(diceNumber) + " is: " + str(value) + "."
		allValues.append(int(value))
		diceNumber += 1
	print "Sum of all dice is " + str(sum(allValues))
	print ""

def playAnotherTime():
	while True:
		playAgain = raw_input("Would you like to roll again? (yes/no): ").lower()
		if playAgain == "no" or playAgain == "n":
			print "Goodbye"
			sys.exit()
		if playAgain == "yes" or playAgain == "y":
			return
		if playAgain != "yes" or playAgain != "y" or playAgain != "no" or playAgain != "n":
			print "You entered something that does not compute. Please try again."
			print ""

#Running the functions
while True:
	rollDice()
	playAnotherTime()