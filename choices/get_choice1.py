from locations.grand_hall import grand_hall
from locations.court_yard import court_yard
from locations.entrance_hall import entrance_hall

option1 = "\n1. the grand hall \n2. the court yard \n3. the entrance hall"


def get_choice1():
    while True:
        print("Where do you want to explore?")
        print("The options are:" + option1)
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
