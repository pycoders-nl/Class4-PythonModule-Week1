# 2- Ders Puani Hesaplama
# Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir.
# Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir.
# Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
# Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.

baslik = "%%%%%%%%%%% Ders Puani Hesaplama %%%%%%%%%%%"
print(baslik.center(44))

ogrenci_adi = input("ogrenci_adi : ")
ogrenci_soyadi = input("ogrenci_soyadi : ")
ogrenci_numarasi = input("ogrenci_numarasi: ")

ders1=input("1. ders adi giriniz: ").upper()
ders2=input("2. ders adi giriniz: ").upper()
ders3=input("3. ders adi giriniz: ").upper()
ders4=input("4. ders adi giriniz: ").upper()

print(ders1, end="")
ders1_vize_notu = int(input(" vize_notu: "))
ders1_final_notu = int(input(" ve final_notu: "))

print(ders2, end="")
ders2_vize_notu = int(input(" vize_notu: "))
ders2_final_notu = int(input(" ve final_notu: "))

print(ders3, end="")
ders3_vize_notu = int(input(" vize_notu: "))
ders3_final_notu = int(input(" ve final_notu: "))

print(ders4, end="")
ders4_vize_notu = int(input(" vize_notu: "))
ders4_final_notu = int(input(" ve final_notu: "))

ders1_yilsonu_ortalamasi = (ders1_vize_notu * 40 / 100) + (ders1_final_notu * 60 / 100)
ders2_yilsonu_ortalamasi = (ders2_vize_notu * 40 / 100) + (ders2_final_notu * 60 / 100)
ders3_yilsonu_ortalamasi = (ders3_vize_notu * 40 / 100) + (ders3_final_notu * 60 / 100)
ders4_yilsonu_ortalamasi = (ders4_vize_notu * 40 / 100) + (ders4_final_notu * 60 / 100)

yilsonu_ortalamalari = [ders1_yilsonu_ortalamasi, ders2_yilsonu_ortalamasi,
                        ders3_yilsonu_ortalamasi, ders4_yilsonu_ortalamasi]
dersler = [ders1,ders2,ders3,ders4]
j = 0
print(baslik.center(44))
for i in yilsonu_ortalamalari:
    if i < 50:
        durum = "   ----> KALDI"
        print(dersler[j], yilsonu_ortalamalari[j], durum)
        j += 1
    elif i >= 50:
        durum = "   ----> GECTI"
        print(dersler[j], yilsonu_ortalamalari[j], durum)
        j += 1
