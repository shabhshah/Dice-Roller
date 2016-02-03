#Rishabh Shah
#2016
#Craps

#imports
import random
import sys
import textwrap

#global variables
global diceValues
diceValues = list(xrange(1,7))
global totalValue
totalValue = 0
global betValue
betValue = 0
global bet
bet = 0

#Defining functions
def rollDice():
	diceValue1 = str(random.choice(diceValues))
	diceValue2 = str(random.choice(diceValues))
	global totalValue
	totalValue = str(int(diceValue2)+int(diceValue1))
	print textwrap.fill("Dice 1 is " + diceValue1 + ".")
	print textwrap.fill("Dice 2 is " + diceValue2 + ".")
	print textwrap.fill("Total value of dice is " + totalValue + ".")

def playAnotherTime():
	while True:
		playAgain = raw_input("Would you like to play again? (yes/no): ").lower()
		if playAgain == "no" or \
		   playAgain == "n":
			print ""
			print textwrap.fill("Goodbye")
			sys.exit()
		if playAgain == "yes" or \
		   playAgain == "y":
			print ""
			return
		if playAgain != "yes" or \
		   playAgain != "y" or \
		   playAgain != "no" or \
		   playAgain != "n":
			print ""
			print textwrap.fill("You entered something that does not compute. Please try again")

def start():
	while True:
		global ifcontinue
		ifcontinue = raw_input("Would you like to play craps? (yes/no): ")
		if ifcontinue == "yes" or \
		   ifcontinue == "y" or \
		   ifcontinue == "no" or \
		   ifcontinue == "n":
			break
		if ifcontinue != "yes" or \
		   ifcontinue != "y" or \
		   ifcontinue != "no" or \
		   ifcontinue != "n":
			print textwrap.fill("You entered something that does compute. Please try again.")

def betting():
	global bet
	while True:
		bet = raw_input("Would you like your bet to be?: $")
		try:
			float(bet)*2
		except:
			print textwrap.fill("You entered something that does compute. Please try again.")
		else:
			break

def game():
	global ifcontinue
	global totalValue
	global bet
	global betValue
	print ""
	start()
	if ifcontinue == "no" or \
	   ifcontinue == "n":
	   	print textwrap.fill("Goodbye.")
		sys.exit()
	print ""

	while True:
		betValue = raw_input("How much money would you like to start off with?: $")
		try:
			float(betValue)*2
		except:
			print textwrap.fill("You entered something that does compute. Please try again.")
		else:
			break

	while True:
		while True:
			betting()
			#first roll
			print ""
			rollDice()
			print ""

			if totalValue == '7' or \
			   totalValue == '11':
				print textwrap.fill("You win.")
				gameState = 0
			elif totalValue == '3':
				print textwrap.fill("You lost.")
				gameState = 1
			elif totalValue == "2":
				print textwrap.fill("Snake eyes!")
				print textwrap.fill("You lost.")
				gameState = 1
			elif totalValue == "12":
				print textwrap.fill("Boxcars!")
				print textwrap.fill("You lost.")
				gameState = 1
			else:
				print textwrap.fill("The point has been established. It is " + totalValue + ".")
				point = totalValue
				gameState = 2
			if gameState == 1:
				betValue = "%.2f" % (float(betValue) - float(float(bet)))
				print textwrap.fill("You bet $" + "%.2f" + ". You now have $" + str(betValue) + ".") % (float(bet))
				break
			elif gameState == 0:
				betValue = "%.2f" % (float(betValue) + float(float(bet)))
				print textwrap.fill("You bet $" + "%.2f" + ". You now have $" + str(betValue) + ".") % (float(bet))
				break

			#going for the point
			while True:
				ifcontinue = raw_input("Would you like to roll for the point? (yes/no): ")
				if ifcontinue == "yes" or \
				   ifcontinue == "y" or \
				   ifcontinue == "n" or \
				   ifcontinue == "no":
					break
				if ifcontinue != "yes" or \
				   ifcontinue != "y" or \
				   ifcontinue != "no" or \
				   ifcontinue != "n":
					print textwrap.fill("You entered something that does compute. Please try again.")
			if ifcontinue == "no" or \
			   ifcontinue == "n":
				break
			
			#rolling the point
			print ""
			while True:
				print textwrap.fill("Rolling...")
				print ""
				rollDice()
				print ""
				if totalValue == point:
					print textwrap.fill("You won.")
					gameState = 0
				elif totalValue == "7":
					print textwrap.fill("You lose.")
					gameState = 1
				elif totalValue == "2":
					print textwrap.fill("Snake eyes!")
					print textwrap.fill("You will have to roll again because the point is " + point + " and that does not equal " + totalValue + ".")
					gameState == 2
				elif totalValue == "12":
					print textwrap.fill("Boxcars!")
					print textwrap.fill("You will have to roll again because the point is " + point + " and that does not equal " + totalValue + ".")
					gameState == 2
				else:
					print textwrap.fill("You will have to roll again because the point is " + point + " and that does not equal " + totalValue + ".")
					gameState == 2
				if gameState == 1:
					betValue = "%.2f" % (float(betValue) - float(float(bet)))
					print textwrap.fill("You bet $" + "%.2f" + ". You now have $" + str(betValue) + ".") % (float(bet))
					break
				elif gameState == 0:
					betValue = "%.2f" % (float(betValue) + float(float(bet)))
					print textwrap.fill("You bet $" + "%.2f" + ". You now have $" + str(betValue) + ".") % (float(bet))
					break

				while True:
					ifcontinue = raw_input("Would you like to roll again? (yes/no): ")
					if ifcontinue == "yes" or \
					   ifcontinue == "y" or \
					   ifcontinue == "no" or \
					   ifcontinue == "n":
						break
					if ifcontinue != "yes" or \
					   ifcontinue != "y" or \
					   ifcontinue != "no" or \
					   ifcontinue != "n":
						print textwrap.fill("You entered something that does compute. Please try again.")
				if ifcontinue == "no" or \
				   ifcontinue == "n":
					break

			break
		playAnotherTime()

print textwrap.fill("Welcome to Rishabh Shah's craps game!")
game()