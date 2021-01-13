from random import randint
#global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#check user's guess against answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

#function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():

    #choosing a random number between 1 to 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number betwee 1 to 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.") 
    #guess a number
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've ran out of guesses, you lose.")
            return #will exit the function
        elif guess != answer:
            print("Guess again.")

game()