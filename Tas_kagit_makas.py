import random  # importing the random module

giris = [' ***************************************************************',
         '*                   TAŞ KAĞIT MAKAS OYUNU                      *',
         '*                                                              *',
         '*      Taş - Makası, Makas Kağıdı, Kâğıt - Taşı yener.         *',
         '*          Aynı obje seçilirse oyun berabere biter             *',
         '*                 Seçiminizi yapınız [1 2 3]                   *',
         '*                                                              *',
         '*                 1) Kullanıcı  - Kullanıcı                    *',
         '*                 2) Bilgisayar - Bilgisayar                   *',
         '*                 3) Bilgisayar - Kullanıcı                    *',
         '*                                                              *',
         '*     Taş Kağıt Makas seçimini  T K M harfleriyle  yapınız     *',
         '*                                                              *',
         ' ***************************************************************']  # Oyun hakkında bilgi

for i in giris:                     # Virgülle ayrılmış giris isimli liste elemanlarını sırayla gez
    print('\t'.expandtabs(), i)     # Her satır başında default olarak 8 boşluk bırakıp liste elemanlarını yazdır


ilk_oyuncu_skor = 0
ikinci_oyuncu_skor = 0
berabere = 0

# print(''' Lutfen oyun modunu seçiminiz
#             1) Kullanıcı  - Kullanıcı
#             2) Bilgisayar - Bilgisayar
#             3) Bilgisayar - Kullanıcı ''')
secim = input()

if secim == "1":
    oyuncu_adi_1 = input("Birinci oyuncunun adini giriniz: ")
    oyuncu_adi_2 = input("İkinci  oyuncunun adini giriniz: ")

    for i in range(10):                                                 #Oyun 10 kez oynanacagi icin dongu kullanilir
        print("\n", i + 1, ". oyun: ")
        ilk_oyuncu_secim = input("Ilk oyuncunun tercihini girin: ")
        ikinci_oyuncu_secim = input("Ikinci oyuncunun tercihini girin: ")
        ilk_oyuncu_secim = ilk_oyuncu_secim.upper()                     #Secimler alinip buyuk harfe cevirilir.
        ikinci_oyuncu_secim = ikinci_oyuncu_secim.upper()

        if ilk_oyuncu_secim == "T" and ikinci_oyuncu_secim == "M":      #Oyunun kurallarina gore kazanan belirlenir
            ilk_oyuncu_skor += 1
        if ilk_oyuncu_secim == "T" and ikinci_oyuncu_secim == "K":
            ikinci_oyuncu_skor += 1
        if ilk_oyuncu_secim == "T" and ikinci_oyuncu_secim == "T":
            berabere += 1

        if ilk_oyuncu_secim == "K" and ikinci_oyuncu_secim == "M":
            ikinci_oyuncu_skor += 1
        if ilk_oyuncu_secim == "K" and ikinci_oyuncu_secim == "T":
            ilk_oyuncu_skor += 1
        if ilk_oyuncu_secim == "K" and ikinci_oyuncu_secim == "K":
            berabere += 1

        if ilk_oyuncu_secim == "M" and ikinci_oyuncu_secim == "T":
            ikinci_oyuncu_skor += 1
        if ilk_oyuncu_secim == "M" and ikinci_oyuncu_secim == "K":
            ilk_oyuncu_skor += 1
        if ilk_oyuncu_secim == "M" and ikinci_oyuncu_secim == "M":
            berabere += 1
    print("\n",oyuncu_adi_1 , "  :", ilk_oyuncu_skor, "kere kazandi.")            #Sonuclar ekrana yazilir
    print(oyuncu_adi_2     , "   :",  ikinci_oyuncu_skor, "  kere kazandi.")
    print("Berabere   :", berabere, "kere bitti. ")

elif secim == "2":                                          #2. secenek bilgisayarin kendi kendine oynamasi
    for i in range(10):
        print("\n", i + 1, ". oyun: ")

        a = (random.randint(1, 3))                          #1 ile 3 arasinda 2 adet random sayi uretilir
        b = (random.randint(1, 3))

        if a == 1:                                          #Sayinin 1 olma durumu Tas, 2: Makas, 3: Kagit olarak atanir
            a = "Tas"
        if a == 2:
            a = "Makas"
        if a == 3:
            a = "Kagit"
        print(a)

        if b == 1:
            b = "Tas"
        if b == 2:
            b = "Makas"
        if b == 3:
            b = "Kagit"
        print(b)

        if a == "Tas" and b == "Makas":                     #Oyunun kurallarina gore kazanan belirlenir
            ilk_oyuncu_skor += 1
        if a == "Tas" and b == "Kagit":
            ikinci_oyuncu_skor += 1
        if a == "Tas" and b == "Tas":
            berabere += 1

        if a == "Kagit" and b == "Makas":
            ikinci_oyuncu_skor += 1
        if a == "Kagit" and b == "Tas":
            ilk_oyuncu_skor += 1
        if a == "Kagit" and b == "Kagit":
            berabere += 1

        if a == "Makas" and b == "Tas":
            ikinci_oyuncu_skor += 1
        if a == "Makas" and b == "Kagit":
            ilk_oyuncu_skor += 1
        if a == "Makas" and b == "Makas":
            berabere += 1

    print("Bilgisayar 1 :", ilk_oyuncu_skor, "kere kazandi.")       #Taraflarin kazanma sayisi ekrana yazdirilir
    print("Bilgisayar 2 :", ikinci_oyuncu_skor, "kere kazandi.")
    print("Berabere     :", berabere, "kere bitti.")

elif secim == "3":                                                  #3. secenekde Kullanici Bilgisayara karsi oynar

    for i in range(10):
        print(i + 1, ". oyun: ")
        tercih = input("Kullanici Secenegi: [T-K-M] ")
        b = tercih.upper()                                          # Kullanici tercihi b olarak atanir
        a = (random.randint(1, 3))

        if a == 1:                                                  # Bilgisayarin secimi a olarak atanir
            a = "T"
        if a == 2:
            a = "M"
        if a == 3:
            a = "K"
        print(a)

        if a == "T" and b == "M":                                   #Oyunun kurallarina gore kazanan belirlenir
            ilk_oyuncu_skor += 1
        if a == "T" and b == "K":
            ikinci_oyuncu_skor += 1
        if a == "T" and b == "T":
            berabere += 1

        if a == "K" and b == "M":
            ikinci_oyuncu_skor += 1
        if a == "K" and b == "T":
            ilk_oyuncu_skor += 1
        if a == "K" and b == "K":
            berabere += 1

        if a == "M" and b == "T":
            ikinci_oyuncu_skor += 1
        if a == "M" and b == "K":
            ilk_oyuncu_skor += 1
        if a == "M" and b == "M":
            berabere += 1

    print("Bilgisayar :", ilk_oyuncu_skor, "kere kazandı.")          #Taraflarin kazanma sayisi ekrana yazdirilir
    print("Kullanici  :", ikinci_oyuncu_skor, "kere kazandı.")
    print("Berabere   :", berabere, "kere bitti.")

else:                                                               # 1,2,3 disinda secim yapilirsa
    print("Yanlış Seçim Yaptınız")                                  # Yanlis Secim mesaji verilir
    print("Sadece [ 1 2 3 ] Seçenekleriniz var")
