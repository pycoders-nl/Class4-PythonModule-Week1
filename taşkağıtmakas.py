oyuncu_1=input("1.oyuncu")
oyuncu_2=input("2.oyuncu")
print("taş,kağıt,makas oyununa hoşgeldiniz,lütfen birbirinizin seçimlerine bakmayınız")
oyuncu_1Skor = 0
oyuncu_2Skor = 0

tur = 10

print("""1->Taş\n2->Kağıt\n3->Makas""")

while True:
    print("Kalan Tur Sayısı \"{}\"".format(tur))
    oyuncu_1=int(input("Oyuncu_1 Seçiminiz Nedir?\n"))
    oyuncu_2=int(input("Oyuncu_2 Seçiminiz Nedir?\n"))
    if (oyuncu_2 == 1):
        print("\n{}\t{}\n".format(oyuncu_1, oyuncu_2))
        if (oyuncu_1 == 1):  # Berabere
            print("Berabere, Skor Yazılmadı..")
        elif (oyuncu_1 == 2):  # Kazanan oyuncu1
            oyuncu_1Skor = oyuncu_1Skor + 1
            print("Oyuncu_1 Kazandı.. Oyuncu_1 = {}, Oyuncu_2 = {}".format(oyuncu_1Skor, oyuncu_2Skor))
            tur = tur - 1
        elif (oyuncu_1 == 3):  # Kazanan oyuncu2
            oyuncu_2Skor = oyuncu_2Skor + 1
            print("Oyuncu_2 kazandı.. Oyuncu_1 = {}, Oyuncu_2 = {}".format(oyuncu_1Skor, oyuncu_2Skor))
            tur = tur - 1
    elif(oyuncu_2 == 2):
        print("\n{}\t{}\n".format(oyuncu_1,oyuncu_2))
        if (oyuncu_1 == 1):    #Kazanan oyuncu2
            oyuncu_2Skor = oyuncu_2Skor + 1
            print("Oyuncu_2 Kazandı.. Oyuncu_1 = {}, Oyuncu_2 = {}".format(oyuncu_1Skor, oyuncu_2Skor))
            tur = tur - 1
        elif (oyuncu_1 == 2):  # Berabere
            print("Berabere, Skor Yazılmadı..")
        elif (oyuncu_1 == 3):  # Kazanan oyuncu1
            oyuncu_1Skor = oyuncu_1Skor + 1
            print("Oyuncu_1 Kazandı.. Oyuncu_1 = {}, Oyuncu_2 = {}".format(oyuncu_1Skor, oyuncu_2Skor))
            tur = tur - 1

        elif (oyuncu_2 == 3):
            print("\n{}\t{}\n".format(oyuncu_1, oyuncu_2))
            if (oyuncu_1 == 1):  # Kazanan oyuncu1
                oyuncu_1 = oyuncu_1 + 1
                print("Oyuncu_1 Kazandı.. Oyuncu_1 = {}, Oyuncu_2 = {}".format(oyuncu_1Skor, oyuncu_2Skor))
                tur = tur - 1
            elif (oyuncu_1 == 2):  # Kazanan oyuncu2
                oyuncu_2Skor = oyuncu_2Skor + 1
                print("Oyuncu_2 Kazandız.. Oyuncu_1 = {}, Oyuncu_2 = {}".format(oyuncu_1Skor, oyuncu_2Skor))
                tur = tur - 1
            elif (oyuncu_1 == 3):  # Berabere
                print("Berabere, Skor Yazılmadı..")

        if (tur == 0):
            print("Oyun Bitti..")
            print("Sonuçlar: Oyuncu_1 = {}, Oyuncu_2 = {}".format(oyuncu_1Skor, oyuncu_2Skor))

            break

