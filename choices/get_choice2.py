from locations.main_doors import main_doors
from locations.court_yard import court_yard
from locations.entrance_hall import entrance_hall

option2 = "\n1. the main doors \n2. the court yard \n3. the entrance hall"


def get_choice2():
    while True:
        print("Where do you want to explore now?")
        print("The options are:" + option2)
        choice2 = input(">")
        if choice2 == "1":
            main_doors()
            break
        elif choice2 == "2":
            court_yard()
            break
        elif choice2 == "3":
            entrance_hall()
            break
        else:
            print("Invalid choice, please try again")
