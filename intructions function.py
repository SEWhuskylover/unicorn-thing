# functions


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


# main


want_intr = yes_no_q("do you need intructions? ")
print(f"you entered {want_intr}")
if want_intr == "yes":
    print(instructions())

