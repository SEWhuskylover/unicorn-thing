# component will let player exit + quit when they are out of money

import random


def generate_token(balance):
    global rounds_played
    rounds_played = 0
    play_again = ""
    # lets the player exit if play_again does = x
    while play_again != "x" and balance != 0:
        rounds_played += 1
        number = random.randint(1, 100)  # chooses token
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4
            print(formatter("!", "great you got a unicorn"))
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1
            print(formatter("o", "you got a donkey"))
        else:
            if number % 2 == 0:
                token = "horse"
                balance -= .50
                print(formatter("H", "you got a horse"))
            else:
                token = "zebra"
                balance -= .50
                print(formatter("Z", "you got a zebra"))
        print(f" \ntoken: {token} \nbalance: ${balance}")
        play_again = input("enter to play again x to exit ").lower()
    return balance


def yes_no_q(question):
    while True:
        answer = input(question).lower()
        if answer == "yes":
            answer = "yes"
            return answer
        elif answer == "no":
            answer = "no"
            return answer
        # if something else error them
        else:
            print("please enter yes or no")


def instructions():
    print("this is a game of luck")
    print("you will pay a doller to play")
    print("you will then be asigned a random animal")
    print("if you get a unicorn you get 5 dollers")
    print("if you get a horse or a zebra you get 50 cents")
    print("if you get a donkey you get nothing")


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottem = symbol * len(formatted_text)
    return f"{top_bottem}\n{formatted_text}\n{top_bottem}"


# main routine
print(formatter("-", "welcome to the lucky unicorn game"))
want_intr = yes_no_q("do you need intructions? ")
print(f"you entered {want_intr}")
if want_intr == "yes":
    print(instructions())

rounds_played = 0
starting_balance = int(input("how much money do you want to play with? \n"))
closing_balance = generate_token(starting_balance)
print(f"\n starting balance was {starting_balance}")
print(f" rounds played { rounds_played}")
print(f" new balance is {closing_balance}")
print(formatter("*", "goodbye"))
