from replit import clear
from art import logo

def find_highest_bidder(bids):
    max_bid =-1
    max_bidder = None
    for key in bids:
        #print(bids[key])
        if bids[key]>max_bid:
            max_bid = bids[key]
            max_bidder = key
    print(f"The winner is {max_bidder} with a bid of ${max_bid}.")

print(logo)
print("Welcome to the secret auction program.")
bidding_finished = False
bids = {}

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What's is your bid? $"))
    bids[name] = bid
    should_continue =  input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if should_continue == "no":
        clear()
        find_highest_bidder(bids)
        bidding_finished = True
    elif should_continue =="yes":
        clear()

   

