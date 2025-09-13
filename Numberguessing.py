#Build a Number Guessing Game (random number 1–100, user keeps guessing until correct).

import random

def numberGuessing():
    
    number=random.randint(1,99)
    guess=0
    
    print(" Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100")

    while guess!=number:
        
        guess = int(input('enter your guess'))
        
        if guess > number:
            print("Too High! Try again.")
        elif guess < number:
            print("Too Low! Try again.")
        else:
            print(" Correct! You guessed the number.")
            
numberGuessing()