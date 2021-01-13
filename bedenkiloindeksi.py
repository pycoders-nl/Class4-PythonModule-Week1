boy=int(input("Boyunuzu giriniz(cm cinsinden): "))
kilo=float(input("kilonuzu giriniz: "))
bki=kilo/((boy/100)**2)
print("Beden kitle index'iniz {}".format(round(bki,2)))
print("Durumunuz: ")
if bki <=24.9:
    print("Normal")
elif bki<=29.9:
    print("Fazla kilolu")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo-24.9*((boy / 100) ** 2)),2))
elif bki<=39.9:
    print("Obez")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))
else:
    print("Aşırı obez")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))