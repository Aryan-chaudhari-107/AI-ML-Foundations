logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

import random



EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Choose difficulty, Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(user_guess, actual_answer, turn):
    if user_guess < actual_answer:
        print("Too low.")
        return turn - 1

    elif user_guess > actual_answer:
        print("Too high.")
        return turn - 1

    elif user_guess == actual_answer:
        print(f"You got it! the answer is {actual_answer}.")



def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    random_number = random.randint(1,101)
    print("I'm thinking of number between 1 to 100.")

    turns = set_difficulty()

    guess = 0
    while guess != random_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, random_number, turns)
        if turns == 0:
            print(f"You've run out of guesses. You lose. the correct ans is {random_number}")
            return
        elif guess != random_number:
            print("Guess again....")

game()