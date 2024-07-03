from options import option1, option2, option3, option4, option5
from grand_hall import grand_hall
from court_yard import court_yard
from entrance_hall import entrance_hall
from main_doors import main_doors
from well import well
from open_gate import open_gate


def get_choice1():
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


def get_choice2():
    while True:
        print("where do you want to explore now?")
        print("the options are:" + option2)
        choice1 = input(">")

        if choice1 == "1":
            main_doors()
            break
        elif choice1 == "2":
            court_yard()
            break
        elif choice1 == "3":
            entrance_hall()
            break
        else:
            print("Invalid choice, please try again")


def get_choice3():
    while True:
        print("where do you want to explore now?")
        print("the options are:" + option3)
        choice1 = input(">")

        if choice1 == "1":
            main_doors()
            break
        elif choice1 == "2":
            well()
            break
        elif choice1 == "3":
            open_gate()
            break
        else:
            print("Invalid choice, please try again")
