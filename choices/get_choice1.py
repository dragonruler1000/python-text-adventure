def get_choice1(controller):
    from locations import grand_hall, court_yard, entrance_hall, library

    while True:
        print("Where do you want to explore?")
        print("The options are:" + controller.option1)
        choice1 = input(">")
        if choice1 == "1":
            grand_hall(controller)
            break
        elif choice1 == "2":
            court_yard(controller)
            break
        elif choice1 == "3":
            entrance_hall(controller)
            break
        elif choice1 == "4":
            library(controller)
            break
        else:
            print("Invalid choice, please try again")
