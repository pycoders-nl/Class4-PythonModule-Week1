
print ("Tas Kagit Makas oyununa hos geldiniz. Oyun 10 el surecektir. \n")

player_1=input("Birinci oyuncunun adini giriniz: ")
player_2=input("Ikinci oyuncunun adini giriniz: ")

player_1_score = 0
player_2_score = 0

count = 0

#Alttaki while blogu oyunun 10 el oynanmasi icin hazirlanmistir.
while count < 10:
    count += 1
    choice_1 = input("Birinci oyuncu Tas, Kagit, Makas secimini yap: ")
    choice_2 = input("Ikinci oyuncu Tas, Kagit, Makas secimini yap: ")

#Alttaki if blogu Tas, Kagit ya da Makas haricinde baska bir deger girilmemesi icin yazilmistir.

    if choice_1=="Tas" or choice_1=="Kagit" or choice_1=="Makas" or choice_2=="Tas" or choice_2=="Kagit" or choice_2=="Makas":
        pass
    else:
        print("lutfen Tas, Kagit, Makas degerlerinden birini giriniz")
        count -= 1

# Alttaki if blogu Tas, Kagit ve Makas secimlerinde hangisinin kazanacagini belirlemek
# ve kazanan oyuncunun skorunu artirmak icin yazilmistir.
    if choice_1 == "Tas" and choice_2 == "Makas":
        player_1_score += 1
    elif choice_1 == "Tas" and choice_2 == "Kagit":
        player_2_score += 1
    elif choice_1 == "Kagit" and choice_2 == "Makas":
        player_2_score += 1
    elif choice_1 == "Kagit" and choice_2 == "Tas":
        player_1_score += 1
    elif choice_1 == "Makas" and choice_2 == "Kagit":
        player_1_score += 1
    elif choice_1 == "Makas" and choice_2 == "Tas":
        player_2_score += 1


#Alttaki if blogu oyuncularin skorlarini karsilastirarak kazanan oyuncuyu belirlemek icin yazilmistir.
if player_1_score > player_2_score:
    print("Tebrikler {}. {} el ustunluk saglayarak kazandin ".format(player_1, player_1_score))
elif player_1_score < player_2_score:
    print("Tebrikler {}. {} el ustunluk saglayarak kazandin ".format(player_2, player_2_score))
else:
    print("Ooops, oyun berabere bitti.")