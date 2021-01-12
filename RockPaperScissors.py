print("-------------------------Stone or Paper or Scissors Game-----------------"
      "\n------------------------------------------------------------------------")

player1=input("First player name ?")                                 # Birinci oyunucunun ismini inputla istiyoruz
player2=input("Second player name ? ")                               # Ikinci oyunucunun ismini inputla istiyoruz
how_many_times = 1                                                   # Oyun 10 tur yapilacagi icin ilk tura 1 yaziyoruz.
score_of_player1 = 0                                                 #Birinci oyuncunun kazandigi scoru
score_of_player2 = 0                                                 #Ikinci oyuncunun kazandigi scoru

while how_many_times < 11:                                           # Oyunu 10 turla kisitliyacak while loop unu yazdik.
    questions1 = input(player1 + " Stone or Paper or Scissors ? \nPlease login as written above ")
                                                            # Ilk oyuncuya tas mi kagit mi makas mi diye soruyoruz.

    questions2 = input(player2 + " Stone or Paper or Scissors ? \nPlease login as written above")
                                                             #Ikinci oyuncuya tas mi kagit mi makas mi diye soruyoruz.


    if questions1=="Stone" and questions2=="Scissors" or questions1== "Paper" and \
            questions2== "Stone" or questions1=="Scissors"and questions2=="Paper":
        score_of_player1 += 1                                # elif kodu ile 1. oyuncunun kazanma olasilillarini
                                                             #and ve or logic leri ile olusturduk
                                                             # ve 1.oyuncunun skorunu 1 arttirdik

    elif questions2=="Stone" and questions1=="Scissors" or questions2== "Paper" and \
            questions1== "Stone" or questions2=="Scissors"and questions1=="Paper":
        score_of_player2 += 1                                # elif kodu ile 2. oyuncunun kazanma olasilillarini
                                                             #and ve or logic leri ile olusturduk ve
                                                             # 2.oyuncunun skorunu 1 arttirdik

    how_many_times += 1                                      #oyundaki tur sayisini 1 arttirdik.
if score_of_player1 > score_of_player2:
    print("Congratulations {0}. You won. Score is  {2}-{3} "
          .format(player1 , player2 , score_of_player1 , score_of_player2))    #if elif else ile sonucu yazdiracak

elif score_of_player2 > score_of_player1:                               # kodu ekledik.
    print("Congratulations {1}. You won. Score is  {3}-{2} "
          .format(player1,player2,score_of_player1,score_of_player2))

else:
    print(" {0} and {1}  No winner.Score is {2}-{3}"
          .format(player1,player2,score_of_player1,score_of_player2))

print("--------------------------------------------------------------------------------------------------------------")