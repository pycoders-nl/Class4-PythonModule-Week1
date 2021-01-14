kullanici_kilo = float(input("Kilonuz:"))
kullanici_boy = float(input("Boy Uzunluğunuz:"))
bki = kullanici_kilo / kullanici_boy**2
print("bki:{}".format(bki))

if bki<25:
    print("NORMAL")
elif 30>bki>=25:
    print("FAZLA KİLOLU")
elif 40>bki>=30:
    print("OBEZ!")
else:
    print("ASIRI SİSMAN!")
