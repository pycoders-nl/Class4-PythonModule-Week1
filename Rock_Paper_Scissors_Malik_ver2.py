"""
**Rock-Paper-Scissors**
* Oyuncularin adlarini alip tas - kagit - makas oyunu oynatiniz.
* Oyun 10 el surecektir. 10 el sonunda kazanan belli olacaktir.
* Skor sonucta gosterilecektir.
"""
while True:
    print("******************************************************\n"
          "***               Rock-Paper-Scissors              ***\n"
          "******************************************************")
    player_1 = input('1st Player Name: ')
    player_1_points = 0

    player_2 = input('2st Player Name: ')
    player_2_points = 0

    tour = 5
    winner = ""

    print("******************************************************\n"
          "***      Please Make your choice in order.         ***\n"
          "******************************************************\n"
          "*        Rock      = [1]                             *\n"
          "*        Paper     = [2]                             *\n"
          "*        Scissors  = [3]                             *\n"
          "******************************************************")

    for i in range(1, tour+1):

        player_1_choice = input('1st Player Choice: ')
        player_2_choice = input('2nd Player Choice: ')

        if (player_1_choice == "1" and player_2_choice == "1") or\
                (player_1_choice == "2" and player_2_choice == "2") or\
                (player_1_choice == "3" and player_2_choice == "3"):
            print(str(i) + ".Round  Rock=Rock Draw")
        elif (player_1_choice == "1" and player_2_choice == "3") or\
                (player_1_choice == "2" and player_2_choice == "1") or\
                (player_1_choice == "3" and player_2_choice == "2"):
            print(str(i) + ".Round  Rock>Scissors Winner Player1")
            player_1_points += 1
        elif (player_1_choice == "1" and player_2_choice == "2") or\
                (player_1_choice == "2" and player_2_choice == "3") or\
                (player_1_choice == "3" and player_2_choice == "1"):
            print(str(i) + ".Round  Paper>Rock Winner Player2")
            player_2_points += 1
        else:
            print("Incorrect input. Try again.")
        i -= 1
        continue

    print("******************************************************\n"
          "***                 Game Over                      ***\n"
          "******************************************************\n")
    if player_1_points == player_2_points:
        winner = "Draw"
        print(f'\n{player_1}:{player_1_points}'
              f'\n{player_2}:{player_2_points}'
              f'\n {winner} !')
    else:
        if player_1_points > player_2_points:
            winner = player_1
        elif player_1_points < player_2_points:
            winner = player_2
        print(f'\n{player_1}:{player_1_points}'
              f'\n{player_2}:{player_2_points}'
              f'\nWINNER is {winner} !')
