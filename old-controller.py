from choices import get_choice1, get_choice2, get_choice3
from locations.court_yard import court_yard


class GameController:
    def __init__(self):
        self.name = ""
        self.option1 = "\n1. the grand hall \n2. the court yard \n3. the entrance hall"
        self.option2 = "\n1. the main doors \n2. the court yard \n3. the entrance hall"
        self.option3 = "\n1. the main doors \n2. the well \n3. the open gate"
        self.playing = True

    def start_game(self):
        self.name = input("What is your name: ")
        print("Welcome " + self.name + " to the castle Jackson")
        self.get_choice1()

    def get_choice1(self):
        from locations.grand_hall import grand_hall
        from locations.entrance_hall import entrance_hall

        while True:
            print("Where do you want to explore?")
            print("The options are:" + self.option1)
            choice1 = input(">")
            if choice1 == "1":
                grand_hall(self)
                break
            elif choice1 == "2":
                court_yard(self)
                break
            elif choice1 == "3":
                entrance_hall(self)
                break
            else:
                print("Invalid choice, please try again")

    def get_choice2(self):
        from locations.main_doors import main_doors
        from locations.entrance_hall import entrance_hall

        while True:
            print("Where do you want to explore now?")
            print("The options are:" + self.option2)
            choice2 = input(">")
            if choice2 == "1":
                main_doors(self)
                break
            elif choice2 == "2":
                court_yard(self)
                break
            elif choice2 == "3":
                entrance_hall(self)
                break
            else:
                print("Invalid choice, please try again")

    def get_choice3(self):
        from locations.main_doors import main_doors
        from locations.well import well
        from locations.open_gate import open_gate

        while True:
            print("Where do you want to explore now?")
            print("The options are:" + self.option3)
            choice3 = input(">")
            if choice3 == "1":
                main_doors(self)
                break
            elif choice3 == "2":
                well(self)
                break
            elif choice3 == "3":
                open_gate(self)
                break
            else:
                print("Invalid choice, please try again")

    def get_choice4(self):
        from locations.court_yard import court_yard
        from locations.maze import maze

        while True:
            print("Head down the latter?")
            choice = input(">")
            choice.lower()
            if choice == "yes" or choice == "y":
                maze()
                break
            elif choice == "no" or choice == "n":
                court_yard()
                break
            else:
                print("please enter a valid option \nvalid options are 'yes, y, no, n'")

    def restart_game(self):
        print("Do you want to restart or exit?")
        choice = input(">")
        if choice.lower() in ["y", "yes", "restart"]:
            self.playing = True
        else:
            self.playing = False

    def run(self):
        while self.playing:
            self.start_game()
            self.restart_game()


# Importing the GameController in main.py
from controller import GameController

if __name__ == "__main__":
    game_controller = GameController()
    game_controller.run()
