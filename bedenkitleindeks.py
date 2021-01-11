# Beden Kitle Indeksi Hesaplama
# Bir kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle
# İndeksi denir. Kısaca insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya
# çıkar. Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç 25'in altindaysa NORMAL,
# '25-30 arasında ise FAZLA KİLOLU, 30-40 arasında ise OBEZ, 40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı yazdiriniz.

while (True):
    kilo_sorgu = float(input("Lutfen Kilonuzu Giriniz:"))
    boy_sorgu = float(input('Lutfen Boyunuzu Giriniz:'))
    normal_bki = round(kilo_sorgu / boy_sorgu ** 2, 2)
    print('Baden Kitle Indeksiniz:', normal_bki)
    if (normal_bki<25):
        print('Beden Kitle indeksiniz NORMAL......')
    elif (25<=normal_bki<30):
        print('Beden Kitle Indeksinize Gore FAZLA KILOLUSUNUZ....')
    elif (30<=normal_bki<40) :
        print('Beden Kitle Indeksinize Gore OBEZSINIZ....')
    elif normal_bki>=40 :
        print('Beden Kitle Endeksinize Gore ASIRI SISMANSINIZ.....')
    break





