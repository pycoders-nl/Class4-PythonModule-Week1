birinci_oyuncu = input("1. oyunucu lutfen adinizi giriniz: ")
ikinci_oyuncu = input("2. oyuncu lutfen adinizi giriniz: ")
sayac = 1
birinci_puan = 0
ikinci_puan = 0
oyun_sayisi = 1
while sayac < 11:
    sayac += 1
    print("Oyun sayisi: ", oyun_sayisi)
    oyun_sayisi += 1
    birinci = int(input("Tas = 1 , Makas = 2, Kagit = 3 seceneklerden birini giriniz: "))
    ikinci = int(input("Tas = 1 , Makas = 2, Kagit = 3 seceneklerden birini giriniz: "))
    if birinci == 1 and ikinci == 1:
        print("Berabere")
    elif birinci == 1 and ikinci == 2:
        print("{} oyuncu kazandi".format(birinci_oyuncu))
        birinci_puan += 1
    elif birinci == 1 and ikinci == 3:
        print("{} oyuncu kazandi".format(ikinci_oyuncu))
        ikinci_puan += 1
    elif birinci == 2 and ikinci == 1:
        print("{} oyuncu kazandi".format(ikinci_oyuncu))
        ikinci_puan += 1
    elif birinci == 2 and ikinci == 2:
        print("Berabere")
    elif birinci == 2 and ikinci == 3:
        print("{} oyuncu kazandi".format(birinci_oyuncu))
        birinci_puan += 1
    elif birinci == 3 and ikinci == 1:
        print("{} oyuncu kazandi".format(birinci_oyuncu))
        birinci_puan += 1
    elif birinci == 3 and ikinci == 2:
        print("{} oyuncu kazandi".format(ikinci_oyuncu))
        ikinci_puan += 1
    elif birinci == 3 and ikinci == 3:
        print("Berabere")
    else:
        print("Eksik var mi")
print("{} puani: {}".format(birinci_oyuncu, birinci_puan))
print("{} puani: {}".format(ikinci_oyuncu, ikinci_puan))
if birinci_puan > ikinci_puan:
    print("Kazanan {}".format(birinci_oyuncu))
elif ikinci_puan > birinci_puan:
    print("Kazanan {}".format(ikinci_oyuncu))
else:
    print("Berabere")
