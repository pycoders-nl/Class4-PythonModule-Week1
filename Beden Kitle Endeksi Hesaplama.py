

print ("Beden Kitle Endeksi Programina Hosgeldiniz: ")

#Asagidaki while dongusu kullanici devam etmek istedigi surece programin calismasi amaciyla yazilmistir.
while True:

    weight = int(input("Lutfen kilonuzu giriniz: "))
    height = float(input("Lutfen boyunuzu metre cinsinden giriniz: "))
    index = (weight/(height**2))
    print ("Beden Kitle endeksiniz: ", index)

#Asagidaki if blogu beden kitle endeksinin bulundugu araliga gore hangi grupta oldugunu belirlemek amaciyla yazilmistir.
    if index < 25 :
        print ("Normal")
    elif index > 25 and index < 30 :
        print ("Fazla Kilolu")
    elif index > 30 and index < 40 :
        print ("Obez")
    elif index > 40 :
        print ("Asiri Sisman")

#Kullanicinin devam etmek mi yoksa programdan cikmak mi istedigini ogrenmek amaciyla yazilmistir.
    comment = input ("\n Cikmak icin Cikis yaziniz, devam etmek icin herhangi bir tusa basiniz ")
    if comment == "Cikis" :
        break