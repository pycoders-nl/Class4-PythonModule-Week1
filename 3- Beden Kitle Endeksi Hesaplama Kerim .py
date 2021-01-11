"""
Bir kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir. 
Kısaca insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya çıkar. 
Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç 
25'in altindaysa NORMAL, 
25-30 arasında ise FAZLA KİLOLU, 
30-40 arasında ise OBEZ, 
40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı yazdiriniz.
"""

while True:
    try:
        boy =  int(input("\nBoyunuzu cm olarak giriniz: "))
        kilo =  int(input("\nKilonuuzu giriniz: "))

        kitle_endeksi = (kilo / (boy ** 2))*10000

        if kitle_endeksi < 25:
            print("\nNORMAL kilodasiniz\n")
        elif 25 < kitle_endeksi < 30:
            print("\nFazla Kilolariniz var dikkatli olmalisiniz!\n")
        elif 30 < kitle_endeksi < 40:
            print("\nOBEZ birisiniz! Diyete baslayiniz!\n")
        elif 40 < kitle_endeksi:
            print("\nAsiri Kilolu birisiniz! Dikkat edin bu durum saglinizi etkileyebilir!\n")

        
    except:
        print("\nHatali giris yaptiniz, Lutfen tekrar deneyiniz!\n")
