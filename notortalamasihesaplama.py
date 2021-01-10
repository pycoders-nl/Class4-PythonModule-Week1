
adi_soyadi = input("Ogrenci'nin Adini ve Soyadini Giriniz:")
okul_numarasi = input("Ogrenci'nin Okul Numarasini Giriniz:")

i=0
while (i<4):


    ders_adi=input("Ders Adini Giriniz Matematik?/Ingilizce?/Muhasebe?/Iktisat?/:")

    if ders_adi=='Matematik':
        mat_vize_notu=int(input("Matematik Vize Notunu Giriniz:"))
        mat_final_notu=int(input("Matematik Final Notunu Giriniz:"))
        mat_ortalama=int((mat_final_notu*0.60)+(mat_vize_notu*0.40))
        # print("Matematik Ders Ortalamasi: ",mat_ortalama)

        matematik_dersi=[ders_adi,mat_vize_notu,mat_final_notu,mat_ortalama]
        i+=0

    elif ders_adi=="Ingilizce":
        ing_vize_notu = int(input("Ingilizce Vize Notunu Giriniz:"))
        ing_final_notu = int(input("Ingilizce Final Notunu Giriniz:"))
        ing_ortalama=int((ing_final_notu*0.60)+(ing_vize_notu*0.40))
        ingilizce_dersi = [ders_adi, ing_vize_notu, ing_final_notu, ing_ortalama]

    elif ders_adi=="Muhasebe":
        muh_vize_notu = int(input("Muhasebe Vize Notunu Giriniz:"))
        muh_final_notu = int(input("Muhasebe Final Notunu Giriniz:"))
        muh_ortalama=int((muh_final_notu*0.60)+(muh_vize_notu*0.40))
        muhasebe_dersi = [ders_adi, muh_vize_notu, muh_final_notu, muh_ortalama]
    elif ders_adi=="Iktisat":
        ikt_vize_notu = int(input("Iktisat Vize Notunu Giriniz:"))
        ikt_final_notu = int(input("Iktisat Final Notunu Giriniz:"))
        ikt_ortalama=int((ikt_final_notu*0.60)+(ikt_vize_notu*0.40))
        iktisat_dersi = [ders_adi, ikt_vize_notu, ikt_final_notu, ikt_ortalama]


print("TUM DERS DETAYLARI ASSAGIDA VERILMISTIR.......")

print("Dersin Adi:{}\nVize Notu:{}\nFinal Notu:{}\nOrtalamasi:{}".format (matematik_dersi[0],matematik_dersi[1],
                                                                          matematik_dersi[2],matematik_dersi[3]))
if mat_ortalama >= 50 :
    print("MATEMATIK DERSINDEN GECTINIZ....")
elif mat_ortalama < 50:
    print("MATEMATIK DERSINDEN KALDINIZ...")

print("Dersin Adi:{}\nVize Notu:{}\nFinal Notu:{}\nOrtalamasi:{}".format (ingilizce_dersi[0],ingilizce_dersi[1],
                                                                          ingilizce_dersi[2],ingilizce_dersi[3]))

if ing_ortalama >= 50:
    print("INGILIZCE DERSINDEN GECTINIZ....")
elif ing_ortalama < 50:
    print("INGILIZCE DERSINDEN KALDINIZ....")

print("Dersin Adi:{}\nVize Notu:{}\nFinal Notu:{}\nOrtalamasi:{}".format (muhasebe_dersi[0],muhasebe_dersi[1],
                                                                          muhasebe_dersi[2],muhasebe_dersi[3]))

if muh_ortalama >= 50:
    print("MUHASEBE DERSINDEN GECTINIZ....")
elif muh_ortalama < 50:
    print("MUHASEBE DERSINDEN KALDINIZ....")

print("Dersin Adi:{}\nVize Notu:{}\nFinal Notu:{}\nOrtalamasi:{}".format (iktisat_dersi[0],iktisat_dersi[1],
                                                                          iktisat_dersi[2],iktisat_dersi[3]))

if ikt_ortalama >= 50:
    print("IKTISAT DERSINDEN GECTINIZ....")
elif ikt_ortalama < 50:
    print("IKTISAT DERSINDEN KALDINIZ....")

print("SISTEMDEN CIKABILIRSINIZ......")

