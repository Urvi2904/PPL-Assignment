#Make a program that randomly chooses a number to guess and then the user will have a few chances to guess the number correctly. In each wrong attempt, the computer will give a hint that the number is greater or smaller than the one you have guessed.

import random
num = random.randrange(1, 51, 1)
guess = 0
max_guesses = 3
count = 0
print("I have chosen a number from 1 to 50.")
while (guess != num) and (count < max_guesses) :
	print("You have " + str(max_guesses - count) + " more guesses.")
	guess = int(input("Make a guess.\n"))
	count += 1
	if (guess < num) and (guess > 0) :
		print("The number is larger than your guess.\n")
	elif (guess > num) and (guess < 51):
		print("The number is smaller than your guess.\n")
	elif (guess == num) and (guess > 0) and (guess < 51) :
		print("Your guess is correct!\n")
	else :
		print("Number is from 1 to 50.\n")

	

