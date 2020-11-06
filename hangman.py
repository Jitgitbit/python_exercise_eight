import random

def hangman():
	word = random.choice(["Venus", "Mars", "Batman", "Pluto", "Moon", "Earth", "Jupiter"])
	validLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	turns = 10
	guessMade = ''

	while len(word) > 0:
		main = ""
		missed = 0

		for letter in word:
			if letter in guessMade:
				main = main + letter
			else:
				main = main + "_" + ""

		if main == word:
			print(main)
			print("You have won this game!")
			break
		
		print("Guess the word: ", main)
		guess = input()

		if guess in validLetters:
			guessMade = guessMade + guess
		else:
			print("Enter a valid character!")
			guess = input()

		if guess not in word:
			turns = turns - 1

name = input("Please enter your name here: ")
print("Welcome" , name)
print("-------------------")
print("Try to guess the word in less than 10 attempts!")
print()
hangman()
print()