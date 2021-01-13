kilo = input("kilonuzu giriniz(kg): ")  # kullanicidan bilgileri alma
boy = input("boyunuzu giriniz(cm): ")
index = int(kilo) / ((int(boy)/100) ** 2)   # alinan degerleri int veri turune cevirerek matematiksel hesaplama ile index elde etme

if index < 25:  # index degerine gore durum degerlendirme
    print("NORMAL")
elif 25 < index < 30:
    print("FAZLA KILOLU")
elif 30 < index < 40:
    print("OBEZ")
elif index > 40:
    print("ASIRI SISMAN")
