# controller.py

from choices.get_choice1 import get_choice1
from choices.get_choice2 import get_choice2
from choices.get_choice3 import get_choice3
from locations.maze import maze

class GameController:
    def __init__(self):
        self.name = ""
        self.option1 = "\n1. the grand hall \n2. the court yard \n3. the entrance hall \n4. the library \n5. the maze"
        self.option2 = "\n1. the main doors \n2. the court yard \n3. the entrance hall \n4. the tower"
        self.option3 = "\n1. the main doors \n2. the well \n3. the open gate"
        self.playing = True
    
    def start_game(self):
        self.name = input("What is your name: ")
        print("Welcome " + self.name + " to the castle Jackson")
        self.get_choice1()

    def get_choice1(self):
        from locations import grand_hall, court_yard, entrance_hall, library

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
            elif choice1 == "4":
                library(self)
                break
            elif choice1 == "5":
                maze(self)  # Pass self as argument
                break
            else:
                print("Invalid choice, please try again")

    def get_choice2(self):
        from locations import main_doors, court_yard, entrance_hall, tower

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
            elif choice2 == "4":
                tower(self)
                break
            else:
                print("Invalid choice, please try again")

    def get_choice3(self):
        from locations import main_doors, well, open_gate

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
        maze(self)  # Ensure maze is called with self

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
