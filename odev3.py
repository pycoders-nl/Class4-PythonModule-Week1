while True:
    print('Kilo ve boyunuzu ornekte oldugu gibi girin. (Ornek:Kg: 75, Boy:1.80) Cikmak icin "q" ya basin.')
    user_kg=input("Kg: ")
    if user_kg=="q":
        print('Programdan cikiliyor...')
        break
    else:
        user_meter=input("Boy: ")
    
    user_kg=int(user_kg)
    user_meter=float(user_meter) 
    islem=(user_kg)/float(user_meter**2) 
  
    
    if islem<=25:
        print(f'Vucut kitle endeksiniz:{int(islem)} (NORMAL)')
    elif islem>=26 and islem<=30:
        print(f'Vucut kitle endeksiniz:{int(islem)} (FAZLA KILOLU)')
    elif islem>=31 and islem<=40:
        print(f'Vucut kitle endeksiniz:{int(islem)} (OBEZ)')
        