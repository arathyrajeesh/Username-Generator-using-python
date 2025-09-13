#Build a Number Guessing Game (random number 1–100, user keeps guessing until correct).

import random

def numberGuessing():
    number = random.randint(1, 100)  
    guess = 0
    attempts = 0
    max_attempts = 7  
    
    print(" Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100")
    print(f"You have {max_attempts} attempts.\n")

    while guess != number and attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1 

        if guess > number:
            print("Too High! Try again.")
        elif guess < number:
            print("Too Low! Try again.")
        else:
            print(f" Correct! You guessed the number in {attempts} tries.")
            return
        

    if guess != number:
        print(f"\n Game Over! You've used all {max_attempts} attempts.")
        print(f"The correct number was: {number}")

numberGuessing()
