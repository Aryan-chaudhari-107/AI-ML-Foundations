
import art
from game_data import data
import random

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_descr}, from {account_country}")

def check_ans(guess, a_followers, b_followers):
    if guess == 'a' and a_followers > b_followers:
        return True
    elif guess == 'b' and b_followers > a_followers:
        return True
    else:
        return False

print(art.logo)
score = 0
game_over = True
account_b = random.choice(data)

while game_over:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}")
    print("\n")

    user_ans = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n"*20)
    print(art.logo)

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = check_ans(user_ans, a_followers_count, b_followers_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = False
