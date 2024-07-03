from grand_hall import grand_hall
from name import name
from options import option1, option2, option3, option4, option5
from court_yard import court_yard
from choices import get_choice1


def game_start():
    print("welcome to my text adventure")
    print("welcome " + name + " to the castle jackson")


def entrance_hall():
    print("you look around and see some stairs leading up to a higher floor")


def main_doors():
    print("you head back to where you started")
    get_choice1()


def well():
    print("you look down the well and see a latter heading down")


def open_gate():
    print("you see that there is a dense forest through the gate")


def restart_game():
    print("do you want to restart or exit")
    choice = input(">")
    if choice == "y" or choice == "yes" or choice == "restart":
        game_start()


# start the game
game_start()
get_choice1()
restart_game()
