""" Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari
 istenecektir. Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir.
 Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır. 
Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir."""

adi = input("Lütfen adınızı giriniz: ")
soyadi = input("Lütfen soyadınızı giriniz: ")
ogrenci_no = input("Lütfen öğrenci numarınızı giriniz: ")
ders_adi_1 = input("Lütfen birinci ders adını giriniz: ")
ders_adi_2 = input("Lütfen ikinci ders adını giriniz: ")
ders_adi_3 = input("Lütfen üçüncü ders adını giriniz: ")
ders_adi_4 = input("Lütfen dördüncü ders adını giriniz: ")
ders1v = int(input("Lutfen {} vize notunu giriniz: ".format(ders_adi_1)))
ders1f = int(input("Lutfen {} final notunu giriniz: ".format(ders_adi_1)))
ders2v = int(input("Lutfen {} vize notunu giriniz: ".format(ders_adi_2)))
ders2f = int(input("Lutfen {} final notunu giriniz: ".format(ders_adi_2)))
ders3v = int(input("Lutfen {} vize notunu giriniz: ".format(ders_adi_3)))
ders3f = int(input("Lutfen {} final notunu giriniz: ".format(ders_adi_3)))
ders4v = int(input("Lutfen {} vize notunu giriniz: ".format(ders_adi_4)))
ders4f = int(input("Lutfen {} final notunu giriniz: ".format(ders_adi_4)))
ders1sonuc = ders1v * 0.3 + ders1f * 0.7
ders2sonuc = ders2v * 0.3 + ders2f * 0.7
ders3sonuc = ders3v * 0.3 + ders3f * 0.7
ders4sonuc = ders4v * 0.3 + ders4f * 0.7
if ders1sonuc >= 50:
    print("Sayin {} {}\n {},{} dersinden KALDINIZ".format(adi, soyadi, ogrenci_no, ders_adi_1))
else:
    print("Sayin {} {}\n {},{} dersinden KALDINIZ".format(adi, soyadi, ogrenci_no, ders_adi_1))

if ders2sonuc >= 50:
    print("Sayin {} {}\n {},{} dersinden KALDINIZ".format(adi, soyadi, ogrenci_no, ders_adi_2))
else:
    print("Sayin {} {}\n {},{} dersinden KALDINIZ".format(adi, soyadi, ogrenci_no, ders_adi_2))

if ders3sonuc >= 50:
    print("Sayin {} {}\n {},{} dersinden KALDINIZ".format(adi, soyadi, ogrenci_no, ders_adi_3))
else:
    print("Sayin {} {}\n {},{} dersinden KALDINIZ".format(adi, soyadi, ogrenci_no, ders_adi_3))

if ders4sonuc >= 50:
    print("Sayin {} {}\n {},{} dersinden KALDINIZ".format(adi, soyadi, ogrenci_no, ders_adi_4))
else:
    print("Sayin {} {}\n {},{} dersinden KALDINIZ".format(adi, soyadi, ogrenci_no, ders_adi_4))



