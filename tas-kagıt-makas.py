oyuncu_1 = input("1. Oyuncunun Adini Giriniz:")
oyuncu_2 = input("2. Oyuncunun Adini Giriniz:")


tkm = ["tas", "kagıt", "makas"]
import random
tas = tkm[0]
kagıt = tkm[1]
makas = tkm[2]

tur = 0
oyuncu_1_skor = 0
oyuncu_2_skor = 0

while tur < 10:
    tur += 1


    print("tur = " + str(tur))
    secim = input("1. oyuncu tas mı? kagıt mı? makas mı? ")
    a = input("2. oyuncu tas mı? kagıt mı? makas mı? ")


#    secim = tkm[random.randint(0, 2)]
#    a = tkm[random.randint(0, 2)]

    print("oyuncu_1", secim, "secti")
    print("oyuncu_2", a, "secti")
    if secim == kagıt:
        if kagıt == a:
            print("Berabere")
        elif tas == a:
            print("1. oyuncu Kazandınız")
            oyuncu_1_skor = oyuncu_1_skor + 1
            print("1. oyuncu: " + str(oyuncu_1_skor) + "\n2. oyuncu: " + str(oyuncu_2_skor) )
        elif makas == a:
            print("2. oyuncu Kazandınız")
            oyuncu_1_skor = oyuncu_1_skor + 1
            print("1. oyuncu: " + str(oyuncu_1_skor) + "\n2. oyuncu: " + str(oyuncu_2_skor))

    elif secim == tas:
        if tas == a:
            print("Berabere")
        elif kagıt == a:
            print("2. oyuncu Kazandınız")
            oyuncu_2_skor = oyuncu_2_skor + 1
            print("1. oyuncu: " + str(oyuncu_1_skor) + "\n2. oyuncu: " + str(oyuncu_2_skor))
        elif makas == a:
            print("1. oyuncu Kazandınız")
            oyuncu_1_skor = oyuncu_1_skor + 1
            print("1. oyuncu: " + str(oyuncu_1_skor) + "\n2. oyuncu: " + str(oyuncu_2_skor))

    elif secim == makas:
        if makas == a:
            print("Berabere")
        elif tas == a:
            print("2. oyuncu Kazandınız")
            oyuncu_2_skor = oyuncu_2_skor + 1
            print("1. oyuncu: " + str(oyuncu_1_skor) + "\n2. oyuncu: " + str(oyuncu_2_skor))
        elif kagıt == a:
            print("1. oyuncu Kazandınız")
            oyuncu_1_skor = oyuncu_1_skor + 1
            print("1. oyuncu: " + str(oyuncu_1_skor) + "\n2. oyuncu: " + str(oyuncu_2_skor))

print("SKOR: ")
print(str(oyuncu_1_skor) + "\n" + str(oyuncu_2_skor))

if(oyuncu_1_skor > oyuncu_2_skor):
    print("Kazanan: 1. oyuncu")
elif(oyuncu_1_skor < oyuncu_2_skor):
    print("Kazanan: 2. oyuncu")
else:
    print("Oyun Berabere Bitti")












