# ask if they want intructions
yes_no_intr = input("do you need intructions? \n")


# if they dont keep going if they do list them
if yes_no_intr == "yes":
    print("instrctions")
elif yes_no_intr == "no":
    print("keep going")


# if something else error them
else:
    print("please enter yes or no")
    while yes_no_intr != "yes" or "no":
        yes_no_intr = input("do you need intructions? \n")
        if yes_no_intr == "yes":
            print("keep going")
        elif yes_no_intr == "no":
            print("intructions")
        else:
            print("please enter yes or no")
