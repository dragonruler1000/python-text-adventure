def grand_hall(controller):
    print(
        "You walk into the grand hall of the castle and see some tables set up but no one in sight"
    )
    print(
        "You hear a voice whisper your name "
        + controller.name
        + " but you still don't see anyone"
    )
    controller.get_choice2()
