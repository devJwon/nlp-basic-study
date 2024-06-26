'''
Guessing Game
I’m thinking of a number between 1 and 100…

What is it?
In a file called game.py, implement a program that:

Prompts the user for a level, 
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.

Hints
Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.'''
import random

def main():
    rand_number =  random.randint(1, 100)

    guess = 0
    while guess != rand_number:
        guess =  int(input("input integer:"))


        if guess > 0:
        #while guess != rand_number:
            if guess < rand_number:
                print("too small")
        
            elif guess > rand_number:
                print("too large")
        else:
            print("please enter a positive number")
    print("you guessed it")


if __name__ == "__main__":
    main()

