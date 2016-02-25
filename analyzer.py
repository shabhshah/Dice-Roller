#Rishabh Shah
#2016
#Mass Dice Roller Analyzer

#imports
import sys
import textwrap
from progressbar import ProgressBar, Percentage, Bar

while True:
	fileToOpen = raw_input("What file to analyze? Include the '.txt' in the name. ")
	try:
		open(fileToOpen)
	except:
		print "You entered something that does not compute. Please try again."
	else:
		break

while True:
	numberOfDice = raw_input("How many dice per line?: ")
	try:
		int(numberOfDice) + 1
	except:
		print "You entered something that does not compute. Please try again."
	else:
		break

diceValues = []

for line in open(fileToOpen):
	line = line.strip

	mainParts = line.split(';')
	sumOfDice = mainParts[1]
	rollsOfDice = mainParts[0]

	individualRollsOfDice = rollsOfDice.split(',')

	x = int(numberOfDice)
	for i in xrange(int(numberOfDice)):
		diceValues.append(individualRollsOfDice[x])
		x -= 1

while True:
	lookFor = raw_input("What number would you like to look for?: ")
	try:
		int(lookFor) + 1
	except:
		print "You entered something that does not compute. Please try again."
	else:
		break

a = diceValues.count(int(lookFor))
b = float(float(a)/float(len(diceValues)))
print "The number of times " + str(lookFor) + " appears is " + str(a) + "."
print "The percentage that " + str(lookFor) + " appears is " + str(b) + "%."