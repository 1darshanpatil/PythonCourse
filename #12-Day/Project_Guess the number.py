#Number guessing game.....
print("The game is about guessing a number.")
#print("The computer will randomly generate a two digit number for the game your task is to guess the number.")
print("The computer will generate a random number for you this game for which you'll have to enter the range in whihc your numbe rshould belong")
import math, random
start, end = int(input("Enter the start of your number.")), int(input("Enter the end of your number."))
number = random.randint(start, end + 1)
chances = int(math.log(end - start, 2)) #Rule of binary chances...
guess = int(input("Enter your number."))
while chances > 0:
	if guess != number:
		chances -= 1
		guess = int(input(f"Chances left {chances}, Try again: "))
	else:
		print("You win")
		break
	
if chances == 0:
	print("Hey look at this looser, Haha!!")
else:
	print("Hey mann you won!!")
