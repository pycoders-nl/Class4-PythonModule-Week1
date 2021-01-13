name = input("Ilk adinizi giriniz: ")
surname = input("Soyadinizi giriniz: ")
student_no = int(input("Ogrenci numaranizi girin: "))
vize = {}
final = {}
ders = {}

for i in range(4):
    ders[i] = input(f"{i+1}. dersin adiniz giriniz: ")
    vize[i] = int(input("Vize notunu girin: "))
    final[i] = int(input("Final notunu giriniz: "))

for i in range(4):
    if (vize[i] * 4/10 + final[i] * 6/10) < 50:
        print(ders[i], "dersinden KALDIN")
    else:
        print(ders[i], "dersinden GECTIN")
