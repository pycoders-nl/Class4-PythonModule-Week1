print('Oyunun Kurallari:..........:')
print('------Tas Makasi kirar-------')
print('------Makas Kagidi keser-----')
print('------Kagit Tasi sarar-------')

oyuncu1skor = 0
oyuncu2skor = 0
i = 0

while i<10:
    i += 1

    oyuncu1 = str(input('1.Oyuncu Lutfen Tahmin Giriniz Tas/Kagit/Makas ?: '))
    oyuncu2 = str(input('2.Oyuncu Lutfen Tahmin Giriniz Tas/Kagit/Makas ?: '))

    if oyuncu1 == oyuncu2:
        print('Ayni Tahmin Bu Yuzden Bu Oyun Berabere......')

    elif oyuncu1 == 'Makas' and oyuncu2 == 'Tas' or oyuncu1 == 'Tas' and oyuncu2 == 'Kagit' or oyuncu1 == 'Kagit' and oyuncu2 == 'Makas':
        print('Oyuncu 2 Oyunu Kazandi  Tebrikler......')
        oyuncu2skor += 1
    elif oyuncu2 == 'Makas' and oyuncu1 == 'Tas' or oyuncu2 == 'Tas' and oyuncu1 == 'Kagit' or oyuncu2 == 'Kagit' and oyuncu1 == 'Makas':
        print('Oyuncu 1 Oyunu Kazandi  Tebrikler......')

        oyuncu1skor += 1


print('Oyuncu 1 Skoru=', oyuncu1skor)
print('Oyuncu 2 Skoru=', oyuncu2skor)
if oyuncu1skor < oyuncu2skor:
    print('OYUN SONU OYUNCU 2 KAZANDI TEBRIKLER............')
elif oyuncu2skor < oyuncu1skor:
    print('OYUN SONU OYUNCU 1 KAZANDI TEBRIKLER............')
else:
    print('OYUN BERABERE.......')


