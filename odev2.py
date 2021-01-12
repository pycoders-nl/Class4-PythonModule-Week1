user = input("Ad Soyad: ")  # kullanicidan giris alinir,
student_no = input("Ogrenci no:")
list = []  # girilen ders isimlerini tutmak icin bos liste olusturulur,
list_not = []  # girilen ders NOTLARI ni tutmak icin bos liste olusturulur,
count = 0  # while dongusunu yeteri sayi giris yapildiginda while dongusunu durdumak icin sayac olusturulur,

while count < 4:  # 4 giris istendigi icin <4 ile dongunun durmasi saglanir,
    count += 1  # her donuste sayac 1 artirilir,

    one_les1 = input('Dersin adini girin: ')  # kullanicidan ders adi istenir,
    # girilen dersin vize notu istenir,
    one_les_vize = int(input(f'{one_les1} vize notu:'))
    # girilen dersin final notu istenir,
    one_les_final = int(input(f'{one_les1} final notu:'))
    # vizenin %40 ile finalin %60 hesaplanarak toplanir arithmetic isimli degiskene atilir,
    arithmetic_ = (one_les_vize*40/100 + one_les_final*60/100)
    # .append ile girilen ders ismi lis isimli listye eklenir,
    list.append(one_les1)
    # .append ile arithmetic degiskenindeki not list_not isimli listeye eklenir,
    list_not.append(arithmetic_)

list_not_len = len(list_not)  # len ile list_not daki item sayisi tespit edilir
# for....range ile item sayisi kadar i degiskenine sirayla atanmasi saglanir,
for i in range(list_not_len):
    if list_not[i] < 50:  # if....[] list_not i. index <50 ise
        # yazilmasi saglanir. (f string i. index ders adi : i. index not
        print(f'{list[i]}:{list_not[i]} Kaldi.')
    else:
        # >50 ise (f string i. index ders adi : i. index not)
        print(f'{list[i]}:{list_not[i]} Gecti.')
