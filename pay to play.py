money_left = int(input("how much money do you wish to add \n max 10 \n min 1 \n "))
check = 1
while check != 2:
    if money_left < 1 or money_left > 10:
        print("please enter a vaild number")
        money_left = int(input("how much money do you wish to add \n max 10 \n min 1 \n "))
    else:
        check = 2
print(f"you now have {money_left} ready to play with")

