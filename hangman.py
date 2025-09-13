#Design a Word Guessing (Hangman) game using a word list.

import random
def Choose_words():
    words=['apple','banana','orange','grapes','strawberry','cherry']
    return random.choice(words)

def display_word(word,guess_letters):
    display=""
    for letter in word:
        if letter in guess_letters:
            display+=letter
        else:
            display+=' _ '
    return display

def hangman():
    word=Choose_words()
    guess_letters=[]
    attempts=6
    print('Welcome to Hangman')
    print('you have 6 attempts try to guess the word !')
    while attempts>0:
        print('\n',display_word(word,guess_letters))
        guess=input('enter the letter: ').lower()
        if guess in guess_letters:
            print('OOPS!, you have already guess this word')
        elif guess in word:
            print('correct guess')
            guess_letters.append(guess)
            if display_word(word,guess_letters)==word:
                print('CONGRATULATION,you win the word is: ',word)
                break
        else:
            print('incorrect guess')
            attempts-=1
            print('you have',attempts,'attempts')
    else:
        print('sorry you have no attempt,the word is:',word)
        
hangman()
    
    