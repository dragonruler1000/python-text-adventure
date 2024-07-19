from locations.maze import maze
from locations.court_yard import court_yard


def get_choice4():
    while True:
        print("Head down the latter?")
        choice = input(">")
        choice.lower()
        if choice == "yes" or choice1 == "y":
            maze()
            break
        elif choice == "no" or choice1 == "n":
            court_yard()
            break
        else:
            print("please enter a valid option \nvalid options are 'yes, y, no, n'")
            