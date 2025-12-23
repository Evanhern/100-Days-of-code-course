import os
from Day_9_assets import logo

def clear_win():
    os.system("cls")
    print(logo)

bidders = {}
highest_bid = 0
highest_bidder = ""
running = True

while running:
    clear_win()
    bidder = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[bidder] = bid
    while True:
        participants = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if participants in ("yes", "no"):
            break
        else:
            print("You did not choose a valid selection. Please type 'yes' or 'no'")

    if participants == "yes":
        continue
    elif participants == "no":
        for key in bidders:
            if bidders[key] > highest_bid:
                highest_bidder = key
                highest_bid = bidders[key]
        clear_win()
        print(f"The winnder is {highest_bidder} with a bid of ${highest_bid}")
        running = False
    