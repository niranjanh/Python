import random

def printDice(no):
	if no == 1:
		print(" ____")
		print("|    |")
		print("| *  |")
		print("|____|")

	elif no == 2:
		print(" ____")
		print("|    |")
		print("| ** |")
		print("|____|")

	elif no == 3:
		print(" ____")
		print("|    |")
		print("|*** |")
		print("|____|")

	elif no == 4:
		print(" ____")
		print("|    |")
		print("| ** |")
		print("| ** |")
		print("|____|")

	elif no == 5:
		print(" ____")
		print("|    |")
		print("| ** |")
		print("| ** |")
		print("|  * |")
		print("|____|")

	elif no == 6:
		print(" ____")
		print("|    |")
		print("| ** |")
		print("| ** |")
		print("| ** |")
		print("|____|")

if __name__ == "__main__":

	play = True

	print("GAME MODES:")
	print("1. Family mode")
	print("2. Global mode")
	# mode = int(input("TYPE the game mode you want to play: "))

	

	whoosePlaying = input("Enter Game Mode: ")

	if whoosePlaying == "1":
		players = ["N", "n", "P", "p", "J", "j", "A", "a"]
	
		while play:
			play = input("Whoose next: ")

			if play not in players:
				play = False
			else:
				play = True
				print("\nYou got: \n\n", printDice(random.randint(1, 6)), end="\n\n")
	else:
		print("\n============================================\nType Exit to End the game.\n===================================\n")
		
		exits = ["Exit", "exit", "EXIT"]		

		while play:
			play = input("Type anything to play: ('Exit' to End.) ")

			if play in exits:
		                play = False
			else:
				play = True
				print("\nYou got: \n\n", printDice(random.randint(1, 6)), end="\n\n")


	print("\n\n---------------------------------------------------------------\nThanks For Playing!!! Come to play Again!!!\n---------------------------------------------------------------\n\n")
