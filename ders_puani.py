# Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir.
# Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir.
# Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
# Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir

ad = input("Ögrencinin Adını giriniz     : ")                    # Ogrenciye ait ad, soyad, numara alinir
soyad = input("Öğrencinin Soyadını giriniz  : ")
no = input("Ögrencinin Numarasını giriniz: ")

dersler = []                                                # Programda kullanilan listeler bos olarak tanimlanir
vizeler = []
finaller = []
ortalamalar = []

for i in range(4):                                          # 4 ders bilgisi icin dongu olusturulur
    ders = input("\n {}. dersin adini giriniz: ".format(i + 1))
    dersler += [ders]
    vize = int(input(" Vize notunu giriniz: "))             # Vize ve final notlari liste elemani olarak atanir
    vizeler += [vize]
    final = int(input(" Final notunu giriniz: "))
    finaller += [final]
    ortalama = (vize * 0.4) + (final * 0.6)                 # Ders ortalamalari hesaplanir
    ortalamalar += [ortalama]                               # hesaplanan ortalama ilgili listeye aktarilir

print("\n--------------------------*------")
print("Öğrenci Bilgileri")
print("---------------------------------")
print("Ogrencinin Adi     : ", ad)
print("Ogrencinin Soyadi  : ", soyad)
print("Ogrencinin Numarasi: ", no)
print("---------------------------------")

print("Ders Bilgileri")
print("---------------------------------")

for i in range(4):                                   # 4 adet ders adi vize ve final, ortalama bilgisi yazdiriliyor
    print("Dersin Adi        : ", dersler[i])
    print("Vize Notu         : ", vizeler[i])
    print("Final Notu        : ", finaller[i])
    print("Dersin Ortalamasi : ", ortalamalar[i])

    if ortalamalar[i] >= 50:                        # Ders ortalamasi 50 ve ustu ise GECTI degilse KALDI yazdiriliyor
        print("Ders Durumu       :  GECTI")
        print("--------------------------------")
    else:
        print("Ders Durumu       :  KALDI")
        print("--------------------------------")
