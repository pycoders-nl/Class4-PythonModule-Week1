"""
Bir kisin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir.
Kısaca insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya çıkar.
Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç 25'in altindaysa NORMAL, 25-30 arasında ise FAZLA KİLOLU,
 30-40 arasında ise OBEZ, 40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı yazdiriniz.
"""
kilo = float(input("Lutfen kilonuzu kg cinsinden yaziniz: "))
boy = float(input("Lutfen boyunuzu metre ve nokta cm yani 1.80 gibi giriniz: "))
kitle_indeksi = kilo / boy ** 2
if kitle_indeksi < 25:
    print("Vucud kitle indeksiniz NORMAL")
elif kitle_indeksi < 30:
    print("Vucud kitle indeksiniz FAZLA KILOLU")
elif kitle_indeksi < 40:
    print("Vucud kitle indeksiniz OBEZ")
else:
    print("Vucud kitle indeksiniz ASIRI SISMAN")
