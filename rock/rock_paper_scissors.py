import random


options=["rock", "paper", "scissors"]
def strat_rock():
    user_wins = 0
    computer_wins = 0
    while True:
        user_input=input("Type Rock/paper/scisser or Q to quit: ").lower()
        if user_input=="q":
            break

        if user_input not in options:
             continue
        random_number=random.randint(0, 2)
        computer_pick=options[random_number]
        print("Computer picked", computer_pick+ ".")

        if user_input=="rock" and computer_pick=="scissor":
            print("You won!")
            user_wins+=1
            continue
        if user_input == "scisser" and computer_pick == "paper":
            print("You won!")
            user_wins += 1
            continue
        if user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
            continue
        else:
            print("you lost!")
            computer_wins+=1
    print("you won", user_wins, "times.")
    print("computer won", computer_wins, "times.")
    print("Goodbye!")