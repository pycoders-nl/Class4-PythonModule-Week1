import math

print("ders puani hesaplama programi \n\n")

ogrenci_ad = input("adinizi girin: ")   # ogrenci bilgilerini alma
ogrenci_soyad = input("soyadinizi girin: ")
ogrenci_numara = input("numaranizi girin: ")
ders_counter = 0    # dongu icin sayac
dersler = {}    # derslerin ortalama notlarini ders isimleriyle birlikte kaydetmek icin kutuphane

while ders_counter < 4: # ders bilgileri almak icin dongu
    ders_counter += 1   # donguyu tamamlamak icin sayac arttirma
    ders = input("ders ismi girin: ")   # ders bilgilerini alma
    ders_vize = input("bu dersin vize notunu girin: ")
    ders_final = input("bu dersin final notunu girin: ")
    ortalama = (int(ders_vize) * 0.4) + (int(ders_final) * 0.6) # alinan vize ve final notlarini int turune cevirerek 
                                                                # yuzdelik hesaplama ile ortalamayi bulma
    dersler[ders] = ortalama    # hesaplanan ortalama notlarini dersler kutuphanesine ders isimlerinin degerleri olarak ekleme

for ders in dersler:    # dersler kutuphanesinde ki her ders icin sonuc yazdiran dongu
    sonuc = dersler[ders] # sonuc degiskeninin degerini dersler kutuphanesinde ki ders degiskeninin degerine esitleme
    if sonuc < 50: # sonuc degerlendirme
        print("%s dersinden GECEMEDINIZ..." % (ders))
    else:
        print("%s dersinden GECTINIZ..." % (ders))

