from art import logo
import os

repeat = 'yes'
bidder = []

while repeat == 'yes':
    os.system("cls")
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidder_dictionary = {"name": name, "bid": bid,}
    bidder.append(bidder_dictionary)

    repeat = input("Are there any other bidders? Type 'yes' or 'no'\n")

winner = bidder[0]
for diction in bidder:

    if(diction["bid"]>winner["bid"]):
        winner = diction

winner_name = winner["name"]
winner_bid = winner["bid"]

print(f"The winner is {winner_name} with a bid of ${winner_bid}.")