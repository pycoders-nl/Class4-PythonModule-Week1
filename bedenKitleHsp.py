# 3- Beden Kitle Indeksi Hesaplama
# Bir kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir.
# Kısaca insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya çıkar.
# Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç 25'in altindaysa NORMAL, 25-30 arasında ise FAZLA KİLOLU, ' \
# '30-40 arasında ise OBEZ, 40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı yazdiriniz.

baslik="%%%%%%%%%%%%%%% Beden Kitle Indeksi Hesaplama %%%%%%%%%%%%%%%"
print(baslik.center(55))
kilo = int(input("Kilonuzu kilogram olarak girin lutfen:      (ornek:63)"))
boy = int(input("Boyunuzu santimetre olarak girin lutfen:      (ornek:172)"))
boy = float(boy / 100)
beden_kitle_endeksi = (kilo / (boy ** 2))
print("Beden Kitle Endeksiniz = ",format(beden_kitle_endeksi,'.2f'))
if beden_kitle_endeksi < 25:
    print("NORMAL")
elif 25 < beden_kitle_endeksi < 30:
    print("FAZLA KILOLU")
elif 30 < beden_kitle_endeksi < 40:
    print("OBEZ")
else:
    print("ASIRI SISMAN")
