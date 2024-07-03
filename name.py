def name():
    while True:
        global name
        name = input("What is your name: ")
        print("your name is " + name)
        a = input("correct: ")
        if a == "yes" or a == "y":
            print("welcome " + name)
            break
        else:
            print("please retype your name")
