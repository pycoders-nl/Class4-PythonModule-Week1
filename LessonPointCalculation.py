print("-------------------------------------------------------------------------------")
print("--------------------------------VIZE-FINAL HESAPLAMA---------------------------")
print("--------------------------------------------------------------------------------")

name= input(" Lutfen adinizi giriniz? : ")                                #Kullanicinin ad soyad ogrenci numarasini
surname= input("Lutfen soyadinizi giriniz? : ")                           # input kullanarak aliyoruz.
student_no= input("Lutfen ogrenci numaranizi giriniz? : ")
my_lessons_list=[]
lesson1= input("Lutfen 1. dersin adini giriniz? : ")                      # 4 tane dersin adini kullanicidan
my_lessons_list.append(lesson1)                                           # isteyerek bos bir my_lessons_list listesine
lesson2= input("Lutfen 2. dersin adini giriniz? : ")                      # gonderiyoruz.
my_lessons_list.append(lesson2)
lesson3= input("Lutfen 3. dersin adini giriniz? : ")
my_lessons_list.append(lesson3)
lesson4= input("Lutfen 4. dersin adini giriniz? :")
my_lessons_list.append(lesson4)
midterm=[]
final=[]
midterm_average=[]
final_average=[]
for i in my_lessons_list:
    midterm.append(int(input(i +" dersinin vize notunu giriniz? : ")))    # for dongusunu kullanarak ders adlarimizin
                                                                          # oldugu listemizden tek tek alarak bu
for i in midterm:                                                         # derslerin vize notlarini alip midterm
    midterm_average.append(float(i*40/100))                               # listesine ekliyoruz.Sonra midterm
                                                                          # listesine vize notlarini tek tek alip
for i in my_lessons_list:                                                 # % 40 ini aldiktan sonra midterm.average
    final.append(int(input(i + " dersinin final notunu giriniz? : ")))    # listesine ekliyoruz.Aynisini final sinavlari
                                                                          # icin %60 ini alarak yapiyoruz.
for i in final:
    final_average.append(float(i*60/100))

if midterm_average[0]+final_average[0]< 50 :
    print(lesson1+" Dersinin ortalamasi = "+str(midterm_average[0]+final_average[0]))
    print("{0} numarali {1} {2} {3} dersininden KALDI ".format(student_no,name,surname,lesson1))
else:
    print(lesson1+" Dersinin ortalamasi = " + str(midterm_average[0] + final_average[0]))
    print("{0} numarali {1} {2} {3} dersininden GECTI ".format(student_no, name, surname, lesson1))
if midterm_average[1]+final_average[1]< 50 :
    print(lesson2 +" Dersinin ortalamasi = "+str(midterm_average[1]+final_average[1]))
    print("{0} numarali {1} {2} {3} dersininden KALDI ".format(student_no,name,surname,lesson2))
else:
    print(lesson2+" Dersinin ortalamasi = " + str(midterm_average[1] + final_average[1]))
    print("{0} numarali {1} {2} {3} dersininden GECTI ".format(student_no, name, surname, lesson2))
if midterm_average[2]+final_average[2]< 50 :
    print(lesson3+" Dersinin ortalamasi = "+str(midterm_average[2]+final_average[2]))
    print("{0} numarali {1} {2} {3} dersininden KALDI ".format(student_no,name,surname,lesson3))
else:
    print(lesson3+" Dersinin ortalamasi = " + str(midterm_average[2] + final_average[2]))
    print("{0} numarali {1} {2} {3} dersininden GECTI ".format(student_no, name, surname, lesson3))
if midterm_average[3]+final_average[3]< 50 :
    print(lesson4+" Dersinin ortalamasi = "+str(midterm_average[3]+final_average[3]))
    print("{0} numarali {1} {2} {3} dersininden KALDI ".format(student_no,name,surname,lesson4))
else:
    print(lesson4+" Dersinin ortalamasi = " + str(midterm_average[3] + final_average[3]))
    print("{0} numarali {1} {2} {3} dersininden GECTI ".format(student_no, name, surname, lesson4))

    # en sonda da dersin ortalamasi 50 nin altinda ise KALDI
    # degilse GECTI notunu yazdiriyoruz.
    # Her ders icin ayri olacak sekilde yapiyoruz.