import random

tokens = ["unicorn", "zebra", "horse", "donkey"]

for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')
