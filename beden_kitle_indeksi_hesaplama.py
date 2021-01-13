#Bir kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir
kilo = int(input("Kilonuzu girin: "))
boy = int(input("Boy uzunlugunuzu girin: "))

if boy > 100:   #boy yazim formatini soylemedik
    boy = boy / 100

index = kilo / boy ** 2
print("Vucud kitle endeksin: ",index)

if index < 25:
    print("NORMAL")
elif index < 30:
    print("FAZLA KILOLU")
elif index < 40:
    print("OBEZ")
else:
    print("ASIRI SISMAN")
