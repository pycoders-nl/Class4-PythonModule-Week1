oyuncu_1 = input("1. Oyuncu Adiniz: ")
oyuncu_2 = input("2. Oyuncu Adiniz: ")

oyuncu_1_skor = 0
oyuncu_2_skor = 0

secenekler = ['Tas', "Kagit", "Makas"]

while(oyuncu_1_skor + oyuncu_2_skor < 10):
    print('\n')
    print(*secenekler, sep=', ')
    print('\n')
    oyuncu_1_secim = input(
        '1. Oyuncu! Lutfen bir secim yapiniz(1 ile 3 arasinda) : ')
    print('\n')
    oyuncu_2_secim = input(
        '2. Oyuncu! Lutfen bir secim yapiniz(1 ile 3 arasinda) : ')
    print('\n')

    if int(oyuncu_1_secim) == 1:
        if int(oyuncu_2_secim) == 1:
            print('Berabere Tekrar Secim Yapiniz')
            print('\n')
        elif int(oyuncu_2_secim) == 2:
            oyuncu_2_skor += 1
            print('{} kazandi. Tebrikler'.format(oyuncu_2))
            print('Skor %d : %d' % (oyuncu_1_skor, oyuncu_2_skor))
            print('\n')
        elif int(oyuncu_2_secim) == 3:
            oyuncu_1_skor += 1
            print('{} kazandi. Tebrikler'.format(oyuncu_1))
            print('Skor %d : %d' % (oyuncu_1_skor, oyuncu_2_skor))
            print('\n')

    if int(oyuncu_1_secim) == 2:
        if int(oyuncu_2_secim) == 2:
            print('Berabere Tekrar Secim Yapiniz')
            print('\n')
        elif int(oyuncu_2_secim) == 1:
            oyuncu_1_skor += 1
            print('{} kazandi. Tebrikler'.format(oyuncu_1))
            print('Skor %d : %d' % (oyuncu_1_skor, oyuncu_2_skor))
            print('\n')
        elif int(oyuncu_2_secim) == 3:
            oyuncu_2_skor += 1
            print('{} kazandi. Tebrikler'.format(oyuncu_2))
            print('Skor %d : %d' % (oyuncu_1_skor, oyuncu_2_skor))
            print('\n')

    if int(oyuncu_1_secim) == 3:
        if int(oyuncu_2_secim) == 3:
            print('Berabere Tekrar Secim Yapiniz')
            print('\n')
        elif int(oyuncu_2_secim) == 1:
            oyuncu_2_skor += 1
            print('{} kazandi. Tebrikler'.format(oyuncu_2))
            print('Skor %d : %d' % (oyuncu_1_skor, oyuncu_2_skor))
            print('\n')
        elif int(oyuncu_2_secim) == 2:
            oyuncu_1_skor += 1
            print('{} kazandi. Tebrikler'.format(oyuncu_1))
            print('Skor %d : %d' % (oyuncu_1_skor, oyuncu_2_skor))
            print('\n')

else:
    print('Oyun Bitti.')
    if oyuncu_1_skor > oyuncu_2_skor:
        print("{} Kazandi. Tebrikler".format(oyuncu_1))
    elif oyuncu_2_skor > oyuncu_1_skor:
        print("{} Kazandi. Tebrikler".format(oyuncu_2))
    else:
        print("Oyun Berabere Tebrikler.")
    print('Skor %d : %d' % (oyuncu_1_skor, oyuncu_2_skor))
