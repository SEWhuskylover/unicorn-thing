# component will let player exit + quit when they are out of money

import random


def generate_token(balance):
    global rounds_played
    rounds_played = 0
    play_again = ""
    # lets the player exit if play_again does = x
    while play_again != "x" and balance != 0:
        rounds_played += 1
        number = random.randint(1, 100)  # can only be donkey
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1
        else:
            if number % 2 == 0:
                token = "horse"
                balance -= .50
            else:
                token = "zebra"
                balance -= .50
        print(f" \ntoken: {token} \nbalance: ${balance}")
        play_again = input("enter to play again x to exit ").lower()
    return balance


# main routine
rounds_played = 0
starting_balance = 5
closing_balance = generate_token(starting_balance)
print(f"\n starting balance was {starting_balance}")
print(f"rounds played { rounds_played}")
print(f" new balance is {closing_balance}")
