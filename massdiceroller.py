#Rishabh Shah
#2016
#Mass Dice Roller

#Imports
import random
import sys
import textwrap
from progressbar import ProgressBar, Percentage, Bar

#Defining Functions
b = """
"""

def playAnotherTime():
	while True:
		playAgain = raw_input("Would you like to roll again? (yes/no): ").lower()
		if playAgain == "no" or playAgain == "n":
			print ""
			print "Goodbye"
			sys.exit()
		if playAgain == "yes" or playAgain == "y":
			return
		if playAgain != "yes" or playAgain != "y" or playAgain != "no" or playAgain != "n":
			print "You entered something that does not compute. Please try again."
			print ""

#Running the functions
print ""
print textwrap.fill("Welcome to the mass dice roller. You will pick the file name, the amount of iterations, the sides on the dice, and how many rolls per iteration.")
while True:
	print ""
	while True:
		times = raw_input("How many iterations would you like?: ")
		try:
			int(times) +1
		except:
			print ""
			print "You entered something that does not copmute. Please try again."
		else:
			break
	print ""
	name = raw_input("What would you like the name of the file to be (leave off the '.txt')?: ") + ".txt"
	print ""
	while True:
			diceSides = raw_input("How many sides per die?: ")
			try:
				int(diceSides) + 1
			except:
				print ""
				print "You entered something that does not compute. Please try again."
			else:
				break
	print ""
	while True:
		numberOfDice = raw_input("How many dice to roll?: ")
		try:
			int(numberOfDice) + 1
		except:
			print ""
			print "You entered something that does not compute. Please try again."
		else:
			break
	fh = open(name, "a")
	print ""
	pbar = ProgressBar()
	for i in pbar(xrange((int(times)))):
		die = []
		possibleDiceValues = list(xrange(1, (int(diceSides)+1)))
		for i in xrange(0, (int(numberOfDice))):
			value = str(random.choice(possibleDiceValues))
			die.append(value)
		c = 0
		for item in die:
			c += int(item)
		die.append(str(c))
		fh.write(",".join(die))
		fh.write(b)
	print ""
	fh.close()
	playAnotherTime()