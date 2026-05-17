
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner}, with a bid of ${highest_bid}.")

game_over = False
bid_data = {}

while game_over == False:
    print(logo)
    name = input("What is your name?: ").lower()
    bid = int(input("What is your bid?: $"))
    bid_data[name] = bid

    new_bidder = input("Are there any other bidders? Type 'YES' or 'NO'.\n").lower()

    if new_bidder == "no":
        game_over = True
        find_highest_bidder(bid_data)
    elif new_bidder == "yes":
        print("\n"*100)
    else:
        print("You can ans only in yes and no.")


