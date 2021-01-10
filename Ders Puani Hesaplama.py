
print ("Ders Puani Hesaplama Programina Hosgeldiniz")

student_name = input ("Lutfen adinizi ve soyadinizi giriniz: ")

#1. dersin adi ve notlarinin istendigi kodlar
lesson_1 = input("Lutfen 1. dersin adini giriniz: ")
midterm_lesson_1 = int(input("Lutfen 1. dersin Vize notunu giriniz: "))
final_lesson_1 = int(input("Lutfen 1. dersin Final notunu giriniz: "))

#2. dersin adi ve notlarinin istendigi kodlar
lesson_2 = input("Lutfen 2. dersin adini giriniz: ")
midterm_lesson_2 = int(input("Lutfen 2. dersin Vize notunu giriniz: "))
final_lesson_2 = int(input("Lutfen 2. dersin Final notunu giriniz: "))

#3. dersin adi ve notlarinin istendigi kodlar
lesson_3 = input("Lutfen 3. dersin adini giriniz: ")
midterm_lesson_3 = int(input("Lutfen 3. dersin Vize notunu giriniz: "))
final_lesson_3 = int(input("Lutfen 3. dersin Final notunu giriniz: "))

#4. dersin adi ve notlarinin istendigi kodlar
lesson_4 = input("Lutfen 4. dersin adini giriniz: ")
midterm_lesson_4 = int(input("Lutfen 4. dersin Vize notunu giriniz: "))
final_lesson_4 = int(input("Lutfen 4. dersin Final notunu giriniz: "))

#Not ortalamlarinin hesaplanmasi
ortalama_not_lesson_1 = int(0.4*midterm_lesson_1 + 0.6*final_lesson_1)
ortalama_not_lesson_2 = int(0.4*midterm_lesson_2 + 0.6*final_lesson_2)
ortalama_not_lesson_3 = int(0.4*midterm_lesson_3 + 0.6*final_lesson_3)
ortalama_not_lesson_4 = int(0.4*midterm_lesson_4 + 0.6*final_lesson_4)

#Yukarida girilen 4 ders ve notlarin gecmeye yeterli olup olmadigini belirleyen 4 adet if blogu

if ortalama_not_lesson_1 > 50 :
    print ("Tebrikler {} dersini {} puan ile gectiniz".format (lesson_1, ortalama_not_lesson_1))
else:
    print ("Uzgunum {} dersinden {} puanla gecemediniz".format(lesson_1, ortalama_not_lesson_1))

if ortalama_not_lesson_2 > 50 :
    print ("Tebrikler {} dersini {} puan ile gectiniz".format (lesson_2, ortalama_not_lesson_2))
else:
    print ("Uzgunum {} dersinden {} puanla gecemediniz".format(lesson_2, ortalama_not_lesson_2))

if ortalama_not_lesson_3 > 50 :
    print ("Tebrikler {} dersini {} puan ile gectiniz".format (lesson_3, ortalama_not_lesson_3))
else:
    print ("Uzgunum {} dersinden {} puanla gecemediniz".format(lesson_3, ortalama_not_lesson_3))

if ortalama_not_lesson_4 > 50 :
    print ("Tebrikler {} dersini {} puan ile gectiniz".format (lesson_4, ortalama_not_lesson_4))
else:
    print ("Uzgunum {} dersinden {} puanla gecemediniz".format(lesson_4, ortalama_not_lesson_4))

