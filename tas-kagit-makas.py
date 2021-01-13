print("""Taş-kâğıt-makas oyununa hosgeldiniz.
    Kurallari zaten biliyorsunuz.\n""")

p1_name = input("1. Oyuncu adini girin: ")       # player_1
p2_name = input("2. Oyuncu adini girin: ")       # player_2

p1_score = 0
p2_score = 0

for i in range(10):
    print(f"""\nTaş makası, makas kağıdı, kağıt da taşı yener.
            Şanslı sayınızı bulun.
    1) Taş
    2) Makas
    3) Kağıt

    {i+1}. tur
    """)

    p1_choice = int(input("1. Oyuncu icin giriniz: "))      # bu sirada birbirlerine bakmamalari gerekiyor elbette :d
    p2_choice = int(input("2. Oyuncu icin giriniz: "))

    fark = p1_choice - p2_choice        # Fark 1 oldugunda, eger negatifse player 1 yenicek, pozitifse player 2 yenicek. 
                                        # Fark 2 oldugunda ise tam tersini uygulayacagiz.

    if fark == 0:
        sonuc = "Beraberlik"    # kazandi
    elif abs(fark) == 1:
        if fark < 0: 
            sonuc = p1_name
            p1_score += 1
        else: 
            sonuc = p2_name
            p2_score += 1
    else:
        if fark > 0: 
            sonuc = p1_name
            p1_score += 1
        else: 
            sonuc = p2_name
            p2_score +=1

    print('\n','#'*10, sonuc, "kazandi", '#'*10)       # sonuc net olark anlasilsin diye boyle yazdim

kazanan = "Beraberlik"

if p1_score > p2_score:
    kazanan = p1_name
elif p2_score > p1_score:
    kazanan = p2_name

print(f"""
##########    Oyun Bitti     #########

{p1_name} in skoru: {p1_score}
{p2_name} in skoru: {p2_score}
Ve {10 - abs(p1_score-p2_score)} el boyunca da beraberlik geldi

########## {kazanan} kazandi #########
""")