#Higher Lower Game Code 

import random
import os
clear = lambda: os.system('cls')

from game_art import logo, vs
from game_data import data

def format_data(account):
    """ Format the account data into printable format """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display game_art
clear()
print(logo)
score = 0
continue_game = True

# Make the game repeatable [till lose]
# Shift the position of B account to A account
"""In this the first choice of b will be created outside the while loop then the uncoming b will the value of a and b will create a new one."""
account_b = random.choice(data)

while continue_game:
    # Generate a random account from the game data [dict values]
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # Ask user for a guess [which one has more insta follower account]
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get follwer count of each account
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    # Clear the screen between rounds.
    clear()
    print(logo)
    # Give user feedback on their game [win or loss each round]
    # Track the score
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final score: {score}")
        




