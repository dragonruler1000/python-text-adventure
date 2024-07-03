def restart_game():
    print("do you want to restart or exit")
    choice = input(">")
    if choice == "y" or choice == "yes" or choice == "restart":
        game_start()
