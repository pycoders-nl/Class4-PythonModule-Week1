

# taş, kağıt, makas oyunu

print ("Taş,Kağıt, Makas oyununa hoş geldiniz")
print ("Rakibiniz bilgisayar...")

tas = 1
kagit = 2
makas = 3

Bil_Skor= 0       # Bilgisayarin Puani
Oyuncu_Skor = 0   # Oyuncunun Puani

oyun_sayi = 10          # Oyun Sayisi Sinirlamasi


while True:
    print("Kalan Oyun Sayısı \"{}\"".format(oyun_sayi))
    import random
    bil_secim = random.randint(1, 3)                #Bilgisayar random ile secim yapiyor
    Oyuncu = int(input("tas ise 1, kagıt ise 2, makas ise 3 tusuna basiniz..."))    #Oyuncunun tercihi

    if(Oyuncu == 1):
        print("\n{}\t{}\n".format(bil_secim,Oyuncu))
        if(bil_secim == 1):     # Berabere
            print("Berabere, Skor Degismedi..")
        elif(bil_secim == 2):   #Kazanan bilgisayar
            Bil_Skor = Bil_Skor + 1
            print("Bilgisayar Kazandı.. Bilgisayar = {}, Oyuncu = {}".format(Bil_Skor,Oyuncu_Skor))
            oyun_sayi = oyun_sayi - 1
        elif(bil_secim == 3):   #Kazanan Oyuncu
            Oyuncu_Skor = Oyuncu_Skor + 1
            print("Siz Kazandız.. Bilgisayar = {}, Oyuncu = {}".format(Bil_Skor,Oyuncu_Skor))
            oyun_sayi = oyun_sayi - 1

    elif(Oyuncu == 2):
        print("\n{}\t{}\n".format(bil_secim,Oyuncu))
        if (bil_secim == 1):    #Kazanan oyuncu
            Oyuncu_Skor = Oyuncu_Skor + 1
            print("Siz Kazandıniz... Bilgisayar = {}, Oyuncu = {}".format(Bil_Skor,Oyuncu_Skor))
            oyun_sayi = oyun_sayi - 1
        elif (bil_secim == 2):  #Berabere
            print("Berabere, Skor Degismedi...")
        elif (bil_secim == 3):  #Kazanan bilgisayar
            Bil_Skor = Bil_Skor + 1
            print("Bilgisayar Kazandı... Bilgisayar = {}, Oyuncu = {}".format(Bil_Skor,Oyuncu_Skor))
            oyun_sayi = oyun_sayi - 1

    elif (Oyuncu == 3):
        print("\n{}\t{}\n".format(bil_secim,Oyuncu))
        if (bil_secim == 1):    #Kazanan cHand
            Bil_Skor = Bil_Skor + 1
            print("Bilgisayar Kazandı.. Bilgisayar = {}, Oyuncu = {}".format(Bil_Skor,Oyuncu_Skor))
            oyun_sayi = oyun_sayi - 1
        elif (bil_secim == 2):  #Kazanan Bilgisayar
            Oyuncu_Skor = Oyuncu_Skor + 1
            print("Siz Kazandız.. Bilgisayar = {}, Oyuncu = {}".format(Bil_Skor,Oyuncu_Skor))
            oyun_sayi = oyun_sayi - 1
        elif (bil_secim == 3):  #Berabere
            print("Berabere,  Skor Degismedi..")

    if oyun_sayi == 0:
        print("10 Tur Bitti...")
        print("Sonuçlar: Bilgisayar = {}, Oyuncu = {}".format(Bil_Skor,Oyuncu_Skor))

        break



