# lets you get a random number
import random
# starting variables
starting_bal = 100
balance = starting_bal
token = ""
# gets a random number
for item in range(100):
    number = random.randint(1, 100)
# gets a token based on that number and adds or removes funds
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1
    else:
        if number %2 == 0:
            token = "horse"
            balance -= .50
        else:
            token = "zebra"
            balance -= .50
# prints token and balance
    print(f" \ntoken: {token} \nbalance: ${balance}")
# prints starting and final balance
print(f"starting balance was {starting_bal}")
print(f"new balance is {balance}")
