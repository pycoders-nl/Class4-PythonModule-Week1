
secenekler=["tas","kagit","makas"]
tas=secenekler[0]
kagit=secenekler[1]
makas=secenekler[2]

oyuncu_1="Erkan"
oyuncu_2="Selim"
oyunsayisi=0
erkanScore=0
selimScore=0

while oyunsayisi<=9:
    Erkan = input("tas mi? kagit mi? makas mi?-ERKAN:")
    Selim = input("tas mi? kagit mi? makas mi?-SELIM:")
    oyunsayisi += 1
    if Erkan == tas:
        if Selim == tas:
            print("Berabere...")
            print("Selim'in Skoru", selimScore)
            print("Erkan'in Skoru", erkanScore)
            continue

        elif Selim == kagit:
            print("Selim kazandi...")
            selimScore += 10
            print("Selim'in Skoru",selimScore)
            print("Erkan'in Skoru",erkanScore)
            continue


        else:
            print("Erkan kazandi...")
            erkanScore += 10
            print("Selim'in Skoru", selimScore)
            print("Erkan'in Skoru", erkanScore)
            continue


    if Erkan == kagit:
        if Selim == tas:
            print("Erkan kazandi...")
            erkanScore += 10
            print("Selim'in Skoru", selimScore)
            print("Erkan'in Skoru", erkanScore)
            continue


        elif Selim == kagit:
            print("Berabere...")
            print("Selim'in Skoru", selimScore)
            print("Erkan'in Skoru", erkanScore)
            continue

        else:
            print("Selim kazandi....")
            selimScore += 10
            print("Selim'in Skoru", selimScore)
            print("Erkan'in Skoru", erkanScore)
            continue


    if Erkan == makas:
        if Selim == tas:
            print("Selim kazandi...")
            selimScore += 10
            print("Selim'in Skoru", selimScore)
            print("Erkan'in Skoru", erkanScore)
            continue


        elif Selim == kagit:
            print("Erkan kazandi...")
            erkanScore += 10
            print("Selim'in Skoru", selimScore)
            print("Erkan'in Skoru", erkanScore)
            continue


        else:
            print("Berabere...")
            print("Selim'in Skoru", selimScore)
            print("Erkan'in Skoru", erkanScore)
            continue

print("Oyun Bitti, Skor Toplamlari:")
print("Selim'in Skoru",selimScore)
print("Erkan'in Skoru",erkanScore)



























