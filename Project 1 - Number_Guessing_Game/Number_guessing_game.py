"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""
import sys
from random import randint

def play_again():
    while True:
        try:
            play = input("Would you like to play again (y/n)?? ")
           
            if play.lower() == 'y':
                start_game()
            
            elif play.lower() == 'n':
                sys.exit("Thanks for playing ! come again soon")

            if play != 'y' or play != 'n':
                raise ValueError
        except ValueError: print("Enter 'y' or 'n' please")    

def start_game():
    print("""
    ***********************************************************************

    Welcome to the number guessing game!! We've generated a random number
    between 1 and 10 for you to guess! let's see if you can get it right, Enjoy! 

    ***********************************************************************
    """)
    random_num = randint(1,10)
    tries = 1

    
    while True:
        try:
            answer = int(input("> "))
        except ValueError:
            print("Please enter numbers only thanks!")
            continue
        if answer == random_num:
            print("Great you nailed it! It took you {} attempts".format(tries))
            break
        elif answer > random_num:
            print("It's lower")
            tries += 1
            continue
        elif answer < random_num:
            print("Its higher")
            tries += 1
            continue

start_game()
play_again()
