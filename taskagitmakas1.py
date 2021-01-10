deger1=str('Makas')
deger2=str('Kagit')
deger3=str('Tas')




skor = 0
while(True):
    print('Oyunumuza Hosgeldiniz Assagida size 10 tahmin sorulacaktir cevaplariniza '
          'gore skorunuz gosterilecektir...')

    Tahmin1=input('1.Tahmini Giriniz Makas?/Tas?/Kagit?: ')
    if deger1==Tahmin1:
        print('Tahmin Ayni Makas BERABERE 2.soruya geciniz......')
    elif deger3==Tahmin1:
        print('Bilgisayarin Tahmini Makas ')
        print('Tas Makasi Kirar KAZANDINIZ TEBRIKLER 2.soruya geciniz ')
        skor+=1
    elif deger2==Tahmin1:
        print('Bilgisayarin Tahmini Makas....')
        print ('Makas Kagidi keser KAYBETTINIZ 2.soruya geciniz.....')
    else:
        print('Degeri Yanlis Girdiginiz Icin Kaybettiniz 2.Soruya Geciniz.....')


    Tahmin2 = input('2.Tahmini Giriniz Makas?/Tas?/Kagit?: ')
    if deger1 == Tahmin2:
        print('Tahmin Ayni Makas BERABERE 3.soruya geciniz......')
    elif deger3 == Tahmin2:
        print('Bilgisayarin Tahmini Makas ')
        print('Tas Makasi kirar KAZANDINIZ TEBRIKLER 3.soruya geciniz ')
        skor += 1
    elif deger2 == Tahmin2:
        print('Bilgisayarin Tahmini Makas....')
        print('Makas Kagidi keser KAYBETTINIZ 3.soruya geciniz.....')
    else:
        print('Degeri Yanlis Girdiginiz Icin Kaybettiniz 3.Soruya Geciniz.....')


    Tahmin3 = input('3.Tahmini Giriniz Makas?/Tas?/Kagit?: ')
    if deger1 == Tahmin3:
        print('Bilgisayarin Tahmini Tas ')
        print('Tas Makasi kirar KAYBETTINIZ 4.soruya geciniz ')
    elif deger2 == Tahmin3:
        print('Bilgisayarin Tahminide Tas ')
        print('Kagit Tasi Sarar KAZANDINIZ TEBRIKLER 4.soruya geciniz ')
        skor += 1
    elif deger3 == Tahmin3:
        print('Bilgisayarin Tahmini Tas....')
        print('Tahmin Ayni Tas BERABERE 4.soruya geciniz...........')
    else:
        print('Degeri Yanlis Girdiginiz Icin Kaybettiniz 4.Soruya Geciniz.....')

    Tahmin4 = input('4.Tahmini Giriniz Makas?/Tas?/Kagit?: ')
    if deger1 == Tahmin4:
        print('Bilgisayarin Tahmini Kagit ')
        print('Makas Kagidi Keser KAZANDINIZ TEBRIKLER 5.soruya geciniz.....')
        skor += 1
    elif deger2 == Tahmin4:
        print('Bilgisayarin Tahminide Kagit ')
        print('Tahmin Ayni Kagit BERABERE 5.Soruya Geciniz...... ')
    elif deger3 == Tahmin4:
        print('Bilgisayarin Tahmini Kagit....')
        print('Kagit Tasi Sarar KAYBETTINIZ 5.soruya geciniz.....')
    else:
        print('Degeri Yanlis Girdiginiz Icin Kaybettiniz 5.Soruya Geciniz.....')

    Tahmin5 = input('5.Tahmini Giriniz Makas?/Tas?/Kagit?: ')
    if deger1 == Tahmin5:
        print('Bilgisayarin Tahmini Makas ')
        print('Tahmin Ayni Makas BERABERE 6.Soruya Geciniz......')
    elif deger2 == Tahmin5:
        print('Bilgisayarin Tahminide Makas ')
        print('Makas Kagidi Keser KAYBETTINIZ 6.soruya geciniz..... ')
    elif deger3 == Tahmin5:
        print('Bilgisayarin Tahmini Makas....')
        print('Tas Makasi Kirar KAZANDINIZ TEBRIKLER 6.soruya geciniz.....')
        skor += 1
    else:
        print('Degeri Yanlis Girdiginiz Icin Kaybettiniz.....')

    Tahmin6 = input('6.Tahmini Giriniz Makas?/Tas?/Kagit?: ')
    if deger1 == Tahmin6:
        print('Bilgisayarin Tahmini Kagit ')
        print('Makas Kagidi Keser KAZANDINIZ TEBRIKLER 7.soruya geciniz.....')
        skor += 1
    elif deger2 == Tahmin6:
        print('Bilgisayarin Tahminide Kagit ')
        print('Tahmin Ayni Kagit BERABERE 7.Soruya Geciniz...... ')
    elif deger3 == Tahmin6:
        print('Bilgisayarin Tahmini Kagit ....')
        print('Kagit Tasi sarar KAYBETTINIZ 7.soruya geciniz.....')
    else:
        print('Degeri Yanlis Girdiginiz Icin Kaybettiniz.....')

    Tahmin7 = input('7.Tahmini Giriniz Makas?/Tas?/Kagit?: ')
    if deger1 == Tahmin7:
        print('Bilgisayarin Tahmini Tas ')
        print('Tas Makasi Kirar KAYBETTINIZ 8.soruya geciniz.....')
    elif deger2 == Tahmin7:
        print('Bilgisayarin Tahminide Tas ')
        print('Kagit Tasi Sarar KAZANDINIZ TEBRIKLER 8.soruya geciniz..... ')
        skor += 1
    elif deger3 == Tahmin7:
        print('Bilgisayarin Tahmini Tas....')
        print('Tahmin Ayni Tas BERABERE 8.Soruya Geciniz......')
    else:
        print('Degeri Yanlis Girdiginiz Icin Kaybettiniz 8.Soruya Geciniz.....')

    Tahmin8 = input('8.Tahmini Giriniz Makas?/Tas?/Kagit?: ')
    if deger1 == Tahmin8:
        print('Bilgisayarin Tahmini Kagit ')
        print('Makas Kagidi Keser KAZANDINIZ TEBRIKLER 9.soruya geciniz.....')
        skor += 1
    elif deger2 == Tahmin8:
        print('Bilgisayarin Tahminide Kagit ')
        print('Tahmin Ayni Kagit BERABERE 9.Soruya Geciniz...... ')
    elif deger3 == Tahmin8:
        print('Bilgisayarin Tahmini Kagit....')
        print('Kagit Tasi Sarar KAYBETTINIZ 9.soruya geciniz.....')
    else:
        print('Degeri Yanlis Girdiginiz Icin Kaybettiniz 9.Soruya Geciniz.....')

    Tahmin9 = input('9.Tahmini Giriniz Makas?/Tas?/Kagit?: ')
    if deger1 == Tahmin9:
        print('Tahmin Ayni Makas BERABERE 10.soruya geciniz......')
    elif deger3 == Tahmin9:
        print('Bilgisayarin Tahmini Makas ')
        print('Tas Makasi kirar KAZANDINIZ TEBRIKLER 10.soruya geciniz ')
        skor += 1
    elif deger2 == Tahmin9:
        print('Bilgisayarin Tahmini Makas....')
        print('Makas Kagidi keser KAYBETTINIZ 10.soruya geciniz.....')
    else:
        print('Degeri Yanlis Girdiginiz Icin Kaybettiniz 10.Soruya Geciniz.....')

    Tahmin10 = input('10.Tahmini Giriniz Makas?/Tas?/Kagit?: ')
    if deger1 == Tahmin10:
        print('Bilgisayarin Tahmini Tas ')
        print('Tas Makasi Kirar KAYBETTINIZ .....')
    elif deger2 == Tahmin10:
        print('Bilgisayarin Tahminide Tas ')
        print('Kagit Tasi Sarar KAZANDINIZ TEBRIKLER ..... ')
        skor += 1
    elif deger3 == Tahmin10:
        print('Bilgisayarin Tahmini Tas....')
        print('Tahmin Ayni Tas BERABERE ......')
    else:
        print('Degeri Yanlis Girdiginiz Icin Kaybettiniz.....')
    break
print('Oyun Bitmistir Oynadiginiz icin TESEKKURLER.........')
print('skorunuz: ', skor)

