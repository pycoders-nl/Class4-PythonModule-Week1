


kullanici_adi = input("Adınız:")
kullanici_soyad = input("Soyadınız:")
kullanici_numara = input("Ogrenci Numaranız:")

derslistem = ["Matematik", "Fizik", "Kimya", "Biyoloji"]
Not_Listesi =[]
for i in derslistem:
    print(i + " dersinin vize notunu giriniz")
    vize_notu = int(input("Vize Notunuz:"))
    Not_Listesi.append(vize_notu)
    print(i + " dersinin final notunu giriniz")
    final_notu = int(input("Final Notunuz:"))
    Not_Listesi.append(final_notu)
    Yil_Sonu_Ortalama = (float(vize_notu) * 0.4) + (float(final_notu) * 0.6)
    print("Yil_Sonu_Ortalama:{}".format(Yil_Sonu_Ortalama))


#print(str(derslistem[0]) + "Dersi Vize Notu:" + str(Not_Listesi[0]) + " Final Notu: " + str(Not_Listesi[1]))
#print(str(derslistem[1]) + "Dersi Vize Notu:" + str(Not_Listesi[2]) + " Final Notu: " + str(Not_Listesi[3]))
#print(str(derslistem[2]) + "Dersi Vize Notu:" + str(Not_Listesi[4]) + " Final Notu: " + str(Not_Listesi[5]))
#print(str(derslistem[3]) + "Dersi Vize Notu:" + str(Not_Listesi[6]) + " Final Notu: " + str(Not_Listesi[7]))

for i in range(0, 4):
    dersAdi = derslistem[i]
    vize_notu = Not_Listesi[i*2]
    final_notu = Not_Listesi[i*2+1]
    Yil_Sonu_Ortalama = (float(vize_notu) * 0.4) + (float(final_notu) * 0.6)

    print(str(dersAdi) + "Dersi Vize Notu:" + str(vize_notu) + " Final Notu: " + str(final_notu))

    if Yil_Sonu_Ortalama < 50:
        print("KALDINIZ!")
    else:
        print("GECTINIZ!")


