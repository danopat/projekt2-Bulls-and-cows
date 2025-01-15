"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - Bulls & Cows

author: Daniel Opat
email: danopat@gmail.com
"""

import random
import time

game_start = time.time()

def greet_player():
    """
    prints basic greeting
    """
    print(
        "Hi there!,",
        "-----------------------------------------------",
        "I've generated a random 4 digit number for you.",
        "Let's play a bulls and cows game.",
        "-----------------------------------------------",
        "Enter a number:",
        "-----------------------------------------------",
        sep="\n"
    )

def generate_secret_number() -> list:
    """
    returns a random secret 4-digit number for the game
    the number shall not start with zero and contains 4 unique digits
    """
    secret_number = [str(random.randint(1, 9))]
    for i in range(3):
        while True:
            another_num = str(random.randint(0, 9))
            if another_num not in secret_number:
                secret_number.append(another_num)
                break
    # print(secret_number) # for testing
    return secret_number

def prompt_player() -> str:
    """
    asks the player for a 4-digit number as his/her guess,
    the number shall not start with zero and shall contain only 4 unique digits,
    anything else does not count as a valid guess
    """
    while True:
        number = input(">>> ")
        if not number.isdigit():
            print("Please enter a 4 digit number, no other characters are allowed.")
        elif len(number) != 4:
            print("Please enter a 4 digit number, not longer or shorter than 4.")
        elif int(number[0]) == 0:
            print("The number cannot start with 0.")
        elif len(set(number)) != 4:
            print("The number cannot contain duplicate digits.")
        else:
            return number


def next_round(guess_count, secret_number):
    """
    provides for a next round of the game:
    counts the number of guesses,
    informs the player about the number of bulls and cows for particular guess,
    ends the game when the secret number is guessed
    """
    guess_count += 1
    players_guess = prompt_player()
    bulls, cows = evaluate_guess(players_guess, secret_number)
    if bulls == 4:
        player_won(guess_count)
    else:
        bulls_text = "bulls"
        cows_text = "cows"
        if bulls == 1:
            bulls_text = "bull"
        if cows == 1:
            cows_text = "cow"
        print(f"{bulls} {bulls_text}, {cows} {cows_text}")
        next_round(guess_count, secret_number)

def player_won(guess_count):
    """
    informs player about the time and number of guesses needed to finish the game
    """
    game_end = time.time()
    player_time = game_end - game_start
    print(f"Correct, you've guessed the right number in {guess_count} guesses")
    print(f"and it took you {int(player_time)} seconds.")
    # TODO - save score to file

def evaluate_guess(player_guess, secret_number) -> tuple:
    """
    returns correct numbers in correct position as bulls
    and correct numbers in incorrect position as cows
    """
    bulls = 0
    cows = 0
    for i in range(0, len(secret_number)):
        if player_guess[i] in secret_number:
            if player_guess[i] == secret_number[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows

greet_player()
next_round(0, generate_secret_number())
