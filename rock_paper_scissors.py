print("rock-paper-scissors game \n")

player1_name = input("enter player1's name: ")  # to get names from players
player2_name = input("enter player2's name: ")
player1_wins = 0    # first scores of players
player2_wins = 0
count = 0   # counter variable to repeat the game as wanted in while loop
choices = ["1", "2", "3"]   # choices for in the game

while count < 10:    # loop for repeating the game
    count += 1  # counter increasing for completing loop

    print("%s's turn" % (player1_name))  # to get choices from players
    player1_choice = input("choose rock(1), paper(2) or scissors(3): ")
    while True:  # to check choice if it's from choices
        if player1_choice not in choices:  # in case the choice is not from choices
            print("please enter 1 , 2 or 3")
            print("%s's turn" % (player1_name))
            player1_choice = input("choose rock(1), paper(2) or scissors(3): ")
        else:
            break # in case the choice is from choices, stops checking

    print("%s's turn" % (player2_name))
    player2_choice = input("choose rock(1), paper(2) or scissors(3): ")
    while True:
        if player2_choice not in choices:
            print("please enter 1 , 2 or 3")
            print("%s's turn" % (player2_name))
            player2_choice = input("choose rock(1), paper(2) or scissors(3): ")
        else:
            break

    if player1_choice == player2_choice:  # in case players choose the same choice
        player1_wins += 1
        player2_wins += 1
    elif player1_choice == "1":
        if player2_choice == "2":
            player2_wins += 1
        else:
            player1_wins += 1
    elif player1_choice == "2":
        if player2_choice == "1":
            player1_wins += 1
        else:
            player2_wins += 1
    elif player1_choice == "3":
        if player2_choice == "1":
            player2_wins += 1
        else:
            player1_wins += 1
    print("\n%s's score: %d \n%s's score: %d\n" %   # to type the current score after each round
          (player1_name, player1_wins, player2_name, player2_wins))

if player1_wins > player2_wins:  # results of game
    print("\n%s WON!" % (player1_name))
elif player2_wins > player1_wins:
    print("\n%s WON!" % (player2_name))
else:
    print("\nTIE!")
