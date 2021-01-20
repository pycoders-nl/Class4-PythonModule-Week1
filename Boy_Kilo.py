print("*<*>* Vucut kitle indeksi hesaplama programi:Hosgeldiniz *<*>*")

boy = int(input("Boyunuzu giriniz (cm):"))
kilo = float(input("Kilonuzu giriniz (kg):"))

vki = kilo / ((boy*boy) / 10000 )

if vki<25:
    print("Vucut kitle endeksiniz {}, VKI=Normal".format(vki))
elif 25<vki<30:
    print("Vucut kitle endeksiniz {}, VKI=!Fazla Kilolu!".format(vki))
elif 30<vki<40:
    print("Vucut kitle endeksiniz {}, VKI=!!Obez!!".format(vki))
else:
    print("Vucut kitle endeksiniz {}, VKI=!!!Asiri Sisman!!!".format(vki))





