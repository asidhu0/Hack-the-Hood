def park():
    print("\nYou got lost in the amusement park. Your goal is to find the exit as soon as possible.")
    print("You come to a crossroad.")
    print("Do you go right (1) or left (2)?")
    print("1). To your right is a path that leads to a delapitated ferry ride.")
    print("2). To your left is a path that leads to a merry go round.")

    answer = input("1 or 2\n")

    if answer == "1":
        print("\nAs you move down the path to the ferry, you find a bright shiny key on the floor. You pick it up.")
    elif answer == "2":
        print("\nYou fall into a pothole and die.")
        game_over("How could you mess this up? There were only two choices.")
        play_again()
    else:
        wrong_choice("You did not make an appropriate choice")
        play_again()

    print("You continue moving forward and find a gate.")
    print("\nYou can go through the gate with the keys that you found (1), or you can move further down along the path(2). (1 or 2)")
    print("1). Unlock the gate and go through.")
    print("2). Continue down the path.")

    response = input("1 or 2\n")

    if response == "1":
        print("\nYou go through the gate and find a janitor that takes you to the exit and you find your family waiting for you.")
        game_over("Congratulations! You escaped the park!")
    elif response == "2":
        print("You continue down the path for all of eternity. You meet a few people along the way until you finally die of starvation.")
        game_over("Make better decisions next time!")
        play_again()
    else:
        wrong_choice("You did not make an appropriate choice")
        play_again()

def play_again():
    reply = input("\nDo you want to play again? Y/N")
    if reply == "Y":
        park()
    elif reply == "N":
        exit()

def game_over(reason):
    print("\n" + reason)
    print("Game Over!")

def wrong_choice(meaning):
    print("\n" + meaning)

park()