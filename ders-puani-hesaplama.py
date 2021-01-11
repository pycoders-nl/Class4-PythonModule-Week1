name = input("Adiniz: ")
lastname = input("Soyadiniz: ")
studen_no = input("Ogrenci numaraniz: ")

lessons = []
for i in range(4):
    print('\n')
    lesson = input("{}. Dersinizi giriniz: ".format(i + 1))
    lessons.append(lesson)

lesson_results = []
for i in range(4):
    print('\n')

    vize = int(
        input("{} Dersiniziz vize notunu giriniz(Sayi olarak): ".format(lessons[i])))
    final = int(
        input("{} Dersiniziz final notunu giriniz(Sayi olarak): ".format(lessons[i])))

    lesson_results.append([vize, final])

print('\n')
print('{} {} oncelikle basarilar diliyorum.'.format(name, lastname))

for i in range(4):
    result = lesson_results[i][0] * 0.4 + lesson_results[i][1] * 0.6
    print('\n')
    if result < 50:
        print("Uzgunum, {} dersinden KALDIN".format(lessons[i]))
    else:
        print("Tebrikler, {} dersini GECTIN".format(lessons[i]))
