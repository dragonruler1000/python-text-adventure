def game_start():
    print("welcome to my text adventure")
    while True:
        name = input("What is your name: ")
        print("your name is " + name)
        a = input("correct: ")
        yes = "yes"
        y = "y"
        if a == yes or a == y:
            print("welcome " + name)
            break
        else:
            print("please retype your name")
    print("welcome " + name + " to the castle jackson")


option1 = "\n1. the grand hall \n2. the court yard \n3. the entrance hall"


def grand_hall():
    print(
        "you walk into the grand hall of the castle and see some tables set up but no one in site"
    )


def court_yard():
    print("you look around and see a well and a open fence")


def entrance_hall():
    print("you look around and see some stairs leading up to a higher floor")


def get_choice():
    while True:
        print("where do you want to explore?")
        print("the options are:" + option1)
        choice1 = input(">")

        if choice1 == "1":
            grand_hall()
            break
        elif choice1 == "2":
            court_yard()
            break
        elif choice1 == "3":
            entrance_hall()
            break
        else:
            print("Invalid choice, please try again")


# start the game
game_start()
get_choice()

# prevent the game from closing immediately
input("Press enter to exit the game.")
