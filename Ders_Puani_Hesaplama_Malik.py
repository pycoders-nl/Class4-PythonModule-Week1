"""
Ders Puani Hesaplama
Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi,
4 ders adi, bu derslerin Vize ve Final notlari istenecektir.
Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir.
Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.
"""

while True:
    print("******************************************************\n"
          "***               Ders Puani Hesaplama             ***\n"
          "******************************************************")
    ad = input('Adınızı Giriniz: ')
    soyad = input('Soyadınızı Giriniz: ')
    numara = input('Ögrenci numaranızı Giriniz: ')

    for i in range(4):  # 4 ders ile ilgili bilgi girişlerini yapmak icin döngü olusturuyoruz
        ders = input("\n {}. dersin adini giriniz: ".format(i+1))
        vize = int(input("\n {}. dersin Vize notunu giriniz: ".format(i+1)))
        final = int(input("\n {}. dersin Final notunu giriniz: ".format(i+1)))
        ort = (vize*40+final*60)/100
        sonuc = "KALDI" if ort < 50 else "GECTI"
        if i == 0:
           ders_1 = [ders, vize, final, ort, sonuc]
        elif i == 1:
           ders_2 = [ders, vize, final, ort, sonuc]
        elif i == 2:
           ders_3 = [ders, vize, final, ort, sonuc]
        elif i == 3:
           ders_4 = [ders, vize, final, ort, sonuc]

    print("******************************************************\n"
          "***                     SONUÇLAR                   ***\n"
          "******************************************************")
    print(f"\n{numara} Numaralı  {ad} , {soyad}  :")
    print("\n{} Dersinden:  {}".format(ders_1[0], ders_1[4]))
    print("\n{} Dersinden:  {}".format(ders_2[0], ders_2[4]))
    print("\n{} Dersinden:  {}".format(ders_3[0], ders_3[4]))
    print("\n{} Dersinden:  {}".format(ders_4[0], ders_4[4]))
    quit()
