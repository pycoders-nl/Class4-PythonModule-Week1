# random modul import edildi.
import random

print("\nTas-kagit-makas oyununun kazanma kurallari asagidaki gibidir: \n"
      + "============================================================= \n"
      + "* Kagit - tas durumunda      (kagit, tasi sarar):   kagit kazanir. \n"
      + "* Tas   - makas durumunda    (tas, makasi kirar):   tas kazanir. \n"
      + "* Makas - kagit durumunda  (makas, kagidi keser):   makas kazanir. \n")

oyuncu_skor = 0
bilg_skor = 0
oyuncu_adi = input("Bir oyuncu adi gir: ").upper()

print("(1) {} once baslasin.\n".format(oyuncu_adi)
      + "(2) BILGISAYAR once baslasin.")

baslangic = int(input("Kim once baslasin? (1 veya 2): "))
i=1
if baslangic == 1:
    while i < 11:
        print("%%%%%%%%%%%% {}. OYUN %%%%%%%%%%%%".format(i))
        print("Bir secim yapiniz (1,2 veya 3) \n 1. Tas \n 2. Kagit \n 3. Makas \n")

        # oyuncudan secim yapmasi istendi.
        print("{} secimini yap! : ".format(oyuncu_adi))
        secim = int(input())

        # kullanici gecerli bir deger girene kadar donguden cikamaz.
        while secim > 3 or secim < 1:
            secim = int(input("1,2 veya 3 rakamlarindan birini girmelisin: "))

        if secim == 1:
            secim_adi = 'Tas'
        elif secim == 2:
            secim_adi = 'Kagit'
        else:
            secim_adi = 'Makas'

        # oyuncunun secimini ekrana yazilir.
        print("{} secimini yapti: ".format(oyuncu_adi) + secim_adi)
        print("\n Oyun sirasi bilgisayarda.......")

        # Bilgisayar random modul den randint() metodunu kullanarak rastgele herhangi bir sayıyı seçer (1,2 veya 3 arasindan)
        bilgisayarin_secimi = random.randint(1, 3)

        # oyuncunun seciminden farkli bir secim yapana kadar, bilgisayar secimini tekrarlar.
        while bilgisayarin_secimi == secim:
            bilgisayarin_secimi = random.randint(1, 3)

        if bilgisayarin_secimi == 1:
            bilg_secim_adi = 'TAS'
        elif bilgisayarin_secimi == 2:
            bilg_secim_adi = 'KAGIT'
        else:
            bilg_secim_adi = 'MAKAS'

        print("Bilgisayarin secimi: " + bilg_secim_adi)
        print(secim_adi + " a karsi " + bilg_secim_adi)

        # kazanma kosullari.
        if (secim == 1 and bilgisayarin_secimi == 2) or (secim == 2 and bilgisayarin_secimi == 1):
            print("Kagit kazanir => ", end="")
            sonuc = "Kagit"

        elif (secim == 1 and bilgisayarin_secimi == 3) or (secim == 3 and bilgisayarin_secimi == 1):
            print("Tas kazanir =>", end="")
            sonuc = "Tas"
        else:
            print("Makas kazanir =>", end="")
            sonuc = "Makas"

        # kimin kazandigini yazdirmak icin
        if sonuc == secim_adi:
            print("                     [ Oyuncu kazandi ]")
            oyuncu_skor += 1
        else:
            print("                     [ Bilgisayar kazandi ]")
            bilg_skor += 1

        i += 1
else:
    while i < 11:
        print("%%%%%%%%%%%% {}. OYUN %%%%%%%%%%%%".format(i))
        print("Bir secim yapiniz (1,2 veya 3) \n 1. Tas \n 2. Kagit \n 3. Makas \n")

        # Bilgisayar random modul den randint() metodunu kullanarak rastgele herhangi bir sayıyı seçer (1,2 veya 3 arasindan)
        bilgisayarin_secimi = random.randint(1, 3)

        print("Bilgisayar secimini yapti! \n" + "sira sende!")
        print("{} secimini yap! : ".format(oyuncu_adi))
        secim = int(input())

        while bilgisayarin_secimi == secim:
            bilgisayarin_secimi = random.randint(1, 3)

        if bilgisayarin_secimi == 1:
            bilg_secim_adi = 'Tas'
        elif bilgisayarin_secimi == 2:
            bilg_secim_adi = 'Kagit'
        else:
            bilg_secim_adi = 'Makas'

        # kullanici gecerli bir deger girene kadar donguden cikamaz.
        while secim > 3 or secim < 1:
            secim = int(input("1,2 veya 3 rakamlarindan birini girmelisin: "))

        if secim == 1:
            secim_adi = 'TAS'
        elif secim == 2:
            secim_adi = 'KAGIT'
        else:
            secim_adi = 'MAKAS'

        # oyuncunun secimini ekrana yazilir.
        print("{} secimini yapti: ".format(oyuncu_adi) + secim_adi)

        print(secim_adi + " a karsi " + bilg_secim_adi)

        # kazanma kosullari.
        if (secim == 1 and bilgisayarin_secimi == 2) or (secim == 2 and bilgisayarin_secimi == 1):
            print("Kagit kazanir => ", end="")
            sonuc = "Kagit"

        elif (secim == 1 and bilgisayarin_secimi == 3) or (secim == 3 and bilgisayarin_secimi == 1):
            print("Tas kazanir =>", end="")
            sonuc = "Tas"
        else:
            print("Makas kazanir =>", end="")
            sonuc = "Makas"

        # kimin kazandigini yazdirmak icin
        if sonuc == secim_adi:
            print("                     [ Oyuncu kazandi ]")
            oyuncu_skor += 1
        else:
            print("                     [ Bilgisayar kazandi ]")
            bilg_skor += 1

        i += 1
# oyun 10 kez oynandiktan sonra while dongusunden cikar.
print("\n %%%%%%%%%%% O Y U N  B I T T I! %%%%%%%%%%% ")
print("{} {} kez kazandi, BILGISAYAR {} kez kazandi".format(oyuncu_adi, oyuncu_skor, bilg_skor))
