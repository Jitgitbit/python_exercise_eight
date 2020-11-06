import random

def hangman():
	word = random.choice(["Venus", "Mars", "Batman", "Pluto", "Moon", "Earth", "Jupiter", "foolish", "retarded", "eloquent", "morbide", "uplifting"])
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
				main = main + "_" + " "

		if main == word:
			print()
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

			if turns == 9:
				print()
				print("9 lives left")
				print(" --------- ")
			if turns == 8:
				print()
				print("8 lives left")
				print(" --------- ")
				print("     O     ")
			if turns == 7:
				print()
				print("7 lives left")
				print(" --------- ")
				print("     O     ")
				print("     |     ")
			if turns == 6:
				print()
				print("6 lives left")
				print(" --------- ")
				print("     O     ")
				print("     |     ")
				print("      \    ")
			if turns == 5:
				print()
				print("5 lives left")
				print(" --------- ")
				print("     O     ")
				print("     |     ")
				print("    / \    ")
			if turns == 4:
				print()
				print("4 lives left")
				print(" --------- ")
				print("     O /   ")
				print("     |     ")
				print("    / \    ")
			if turns == 3:
				print()
				print("3 lives left")
				print(" --------- ")
				print("   \ O /   ")
				print("     |     ")
				print("    / \    ")
			if turns == 2:
				print()
				print("2 lives left, watch out for the noose!")
				print(" --------- ")
				print("   \ O / | ")
				print("     |   O ")
				print("    / \    ")
			if turns == 1:
				print()
				print("1 life left, last breath!")
				print(" --------- ")
				print("    \O_|   ")
				print("     |\    ")
				print("    / \    ")
			if turns == 0:
				print()
				print("0 lives left, your attempt of winning this game has failed completely! You lost, and your man is dead!")
				print(" --------- ")
				print("     |     ")
				print("     O     ")
				print("    /|\    ")
				print("    / \    ")
				break

name = input("Please enter your name here: ")
print("Welcome" , name)
print("-------------------")
print("Try to guess the word! You can only make 10 mistakes!")
print()
hangman()
print()