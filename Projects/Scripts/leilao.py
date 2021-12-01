logo = '''
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


from os import system

print(logo)


def find_highest_bidder(bidding_record):
    # bidding-record = {"Angela": 123, "james": 321}
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with $ {highest_bid}")

# Main Program

bids = {}
biddins_finished = False


while(not biddins_finished):
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other biddins? Type 'Yes' or 'No': ").lower()
    if should_continue == 'no':
        biddins_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        system("clear")

# ---- END ----#