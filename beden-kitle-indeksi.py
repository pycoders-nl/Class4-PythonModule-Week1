weight = int(input("Kilonuzu Giriniz Lutfen Rakam ile (KG): "))
height = float(input("Boyunuzu Giriniz Lutfen Rakam ile (m): "))

result = weight / (height ** 2)

if result < 25:
    print('NORMAL')
elif result >= 25 and result < 30:
    print("FAZLA KILOLU")
elif result >= 30 and result < 40:
    print("OBEZ")
else:
    print("AŞIRI ŞİŞMAN")
