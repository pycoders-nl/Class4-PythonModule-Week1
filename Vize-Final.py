ad=input("Ogrencinin Adi: ")
soyad=input("Ogrencinin Soyadi: ")
no=input("Ogrencinin Numarasi: ")

bilgiler=[ad,soyad,no]

print("Ogrecinin Adi: {}\nOgrecinin Soyadi: {}\nOgrecinin Numarasi: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

vize=input("Mat_1-Vize: ")
final=input("Mat_1-Final: ")
ortalama=(float(vize)*0.4)+(float(final)*0.6)
print("Ortalama:{0}".format(ortalama))
if(ortalama<50):
    print("Kaldiniz...")
else:
    print("Gectiniz...")

vize=input("Fiz_1-Vize: ")
final=input("Fiz_1-Final: ")
ortalama=(float(vize)*0.4)+(float(final)*0.6)
print("Ortalama:{0}".format(ortalama))
if(ortalama<50):
    print("Kaldiniz...")
else:
    print("Gectiniz...")

vize=input("Kim_1-Vize: ")
final=input("Kim_1-Final: ")
ortalama=(float(vize)*0.4)+(float(final)*0.6)
print("Ortalama:{0}".format(ortalama))
if(ortalama<50):
    print("Kaldiniz...")
else:
    print("Gectiniz...")

vize=input("Bio_1-Vize: ")
final=input("Bio_1-Final: ")
ortalama=(float(vize)*0.4)+(float(final)*0.6)
print("Ortalama:{0}".format(ortalama))
if(ortalama<50):
    print("Kaldiniz...")
else:
    print("Gectiniz...")








