import random

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    # Get the level from the user
    level = get_positive_integer("Level: ")

    # Generate a random number between 1 and the level (inclusive)
    number_to_guess = random.randint(1, 100)

    while True:
        # Get the user's guess
        guess = get_positive_integer("Guess: ")

        # Compare the guess with the generated number
        if guess < number_to_guess:
            print("Too small!")
        elif guess > number_to_guess:
            print("Too large!")
        else:
            print("Just right!")
            break

    main()