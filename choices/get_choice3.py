from locations.main_doors import main_doors
from locations.well import well
from locations.open_gate import open_gate

option3 = "\n1. the main doors \n2. the well \n3. the open gate"


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
