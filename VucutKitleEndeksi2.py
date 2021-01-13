
# Beden Kitle Indeksi Hesaplama

boy=int(input("Boyunuzu giriniz (cm): "))
kilo=float(input("kilonuzu giriniz: "))
vki=kilo/((boy/100)**2)
print("Vücut kitle index'iniz {}".format(round(vki,1)))
print("Degerlendirme: ")
if vki <25:
    print("Normal")
elif vki <30:
    print("Fazla kilolu")
elif vki<40:
    print("Obez")
else:
    print("Aşırı Sisman")