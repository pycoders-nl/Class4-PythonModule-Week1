"""
Beden Kitle Indeksi Hesaplama
Bir kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir.
Kısaca insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya çıkar.
Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç
25'in altindaysa NORMAL,
25-30 arasında ise FAZLA KİLOLU,
30-40 arasında ise OBEZ,
40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı yazdiriniz.
"""
while True:
    print("******************************************************\n"
          "***      Beden Kitle Indeksi Hesaplama             ***\n"
          "******************************************************")
    kilo = float(input('Ağırlığınızı kg olarak giriniz: '))
    boy = float(input('Boyunuzu m olarak giriniz: '))
    indeks = kilo / (boy**2)
    if indeks < 25 :
        print("NORMAL")
    elif indeks > 25 and indeks <= 30:
        print("FAZLA KİLOLU")
    elif indeks > 30 and indeks <= 40:
        print("OBEZ")
    else:
        print("AŞIRI ŞİŞMAN")
