"""
Guess the number game
"""

import random


def start_game():
    """Initialize game and return random number to guess"""
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    return random.randint(1, 100)


def get_guess():
    """Get user's guess."""
    while True:
        try:
            guess = int(input("What's your guess? "))
            if 1 <= guess <= 100:
                return guess
            print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def check_guess(guess, answer):
    """Compare guess to answer and print result."""
    if guess == answer:
        print(f"Congratulations! {guess} was the number.")
    elif guess < answer:
        print("Too low, try again!")
    else: 
        print("Too high, try again!")


def play_game():
    """Play a full game."""
    answer = start_game()
    while True:
        guess = get_guess()
        check_guess(guess, answer)
        if guess == answer:
            break

    print("Thanks for playing!")


if __name__ == '__main__':
    # Only run game if executed, not when imported
    play_game()
