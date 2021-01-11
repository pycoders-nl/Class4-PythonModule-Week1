# Kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir.
# Insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya çıkar.
#
print("Merhaba, Bu Program Beden Kitle Indeksinizi Hesaplar! ")
kilo = float(input("Agirliginizi kg olarak giriniz: "))             # Kullanicinin agirligi alinip "kilo" ya atanir
boy = float(input("Boyunuzu metre olarak giriniz: "))               # Kullanicinin boyu alinip "boy" a atanir
beden_kitle_indexi = kilo / (boy * boy)                             # beden_kitle_indexi hesaplanir

print("\nBeden Kitle Indeksiniz: ", round(beden_kitle_indexi, 2))   # Sonuc kusuratli kisim 2 basamak olarak yazdirirlir

if beden_kitle_indexi < 25:                                         # Islem sonucuna gore mesaj yazilir
    print("Normal")

elif beden_kitle_indexi < 30:
    print("Fazla Kilolu")

elif beden_kitle_indexi < 40:
    print("Obez")

else:
    print("Asiri Sisman")
