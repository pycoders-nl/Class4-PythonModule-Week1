 #Yil Sonu Ders Degerlendirme modulu
"""Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi,
4 ders adi, bu derslerin Vize ve Final notlari istenecektir.
Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir.
Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir."""
print("Yil Sonu Ders Degerlendirme Programi")
print("Asagiya isminizi, ogrenci mumaranizi, 4 ders ismini, bunlarin Vize ve Final Sonuclarini giriniz")
Ad= input ("Adiniz :")
Soyad= input ("Soyadiniz :")
Ogrenci_No= input("Ogrenci No:")
Ders1= input("1.Ders:")
print (Ders1 + ' vize ve final sonuclarini giriniz, 0-100 arasi')
Ders_1_Vz= input(Ders1 + ' Vize Sonucu :')
Ders_1_Fnl= input(Ders1 + ' Final Sonucu :')
Ders1_Ort= ((int(Ders_1_Vz)* 0.40)+(int(Ders_1_Fnl) * 0.60))
Ders2= input("2.Ders:")
print (Ders2 + ' vize ve final sonuclarini giriniz, 0-100 arasi')
Ders_2_Vz= input(Ders2 + ' Vize Sonucu :')
Ders_2_Fnl= input(Ders2 + ' Final Sonucu :')
Ders2_Ort= ((int(Ders_2_Vz)* 0.40)+(int(Ders_2_Fnl) * 0.60))
Ders3= input("3.Ders:")
print (Ders3 + ' vize ve final sonuclarini giriniz, 0-100 arasi')
Ders_3_Vz= input(Ders3 + ' Vize Sonucu :')
Ders_3_Fnl= input(Ders3 + ' Final Sonucu :')
Ders3_Ort= ((int(Ders_3_Vz)* 0.40)+(int(Ders_3_Fnl) * 0.60))
Ders4= input("4.Ders:")
print (Ders4 + ' vize ve final sonuclarini giriniz, 0-100 arasi')
Ders_4_Vz= input(Ders4 + ' Vize Sonucu :')
Ders_4_Fnl= input(Ders4 + ' Final Sonucu :')
Ders4_Ort= ((int(Ders_4_Vz)* 0.40)+(int(Ders_4_Fnl) * 0.60))
print ('Sonuclariniz degerlendiriliyor....')
if ((int(Ders_1_Vz)* 0.40)+(int(Ders_1_Fnl) * 0.60)) >= 50:
        print (Ders1, '-', 'Yil Sonu Ortalama:', int(Ders1_Ort), 'GECTI')
else:
    print (Ders1, 'Yil Sonu Ortalama:', int(Ders1_Ort), 'KALDI')
if ((int(Ders_2_Vz)* 0.40)+(int(Ders_2_Fnl) * 0.60)) >= 50:
        print (Ders2, '-', 'Yil Sonu Ortalama:', int(Ders2_Ort), 'GECTI')
else:
    print (Ders2, '-', 'Yil Sonu Ortalama:', int(Ders2_Ort),'KALDI')
if ((int(Ders_3_Vz)* 0.40)+(int(Ders_3_Fnl) * 0.60)) >= 50:
        print (Ders3, '-', 'Yil Sonu Ortalama:', int(Ders3_Ort), 'GECTI')
else:
    print (Ders3, '-', 'Yil Sonu Ortalama:', int(Ders3_Ort), 'KALDI')
if ((int(Ders_4_Vz)* 0.40)+(int(Ders_4_Fnl) * 0.60)) >= 50:
        print (Ders4, '-', 'Yil Sonu Ortalama:', int(Ders4_Ort), 'GECTI')
else:
    print (Ders4, '-', 'Yil Sonu Ortalama:', int(Ders4_Ort), 'KALDI')

