#Number gussing Game
#Author: Omaia
#Date: 2025.08.16
import random

print("let me blow your mind!!")

# Computer chooses a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
guess = 0

# Loop until the player guesses correctly
while guess != secret_number:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("you touched the ground bro! Try again.")
    elif guess > secret_number:
        print("you fly away dude! Try again.")
    else:
        print(f" Congratulations! You guessed the number {secret_number} in {attempts} tries.")
        #a simple guissing number game created by me and written in (python)*.
    #a computer randomly selects a number between 1 and 100 and the player has to guess

