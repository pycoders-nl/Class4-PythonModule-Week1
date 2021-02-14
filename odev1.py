player_1=input("Oyuncu1 adinizi girin: ")#birinci oyuncu dan adi istenir,
player_2=input("Oyuncu2 adinizi girin: ")#ikinci oyuncudan adi istenir,

t="tas"
k="kagit" #tas, kagit , makas t,k,m degiskenlerine atanir,
m="makas"

player1_skor=0 #oyuncu1 skorlarrini toplami icin olusturulur,
player2_skor=0 #oyuncu2 skorlarinin toplami icin olusturulur,
p1_list=[]
p2_list=[]
game=0 #while dongusunun durmasi saglamak icin olusturulur, 

print('Lutfen Tas icin "T", Kagit icin "K", Makas icin "M harfine basin')#oyun kullanicilara bilgilendirme yapilir.
while game<10: #game<10 ile 10 oyun sonunda dongu bitirilir,
    game+=1 #her dongude game 1 eklenir 
    player1_move=input( f'{player_1}:')#oyuncu1 den  hamle istenir,
    player1_move=player1_move.lower() #girilen deger kucuk harfe donusturulur,
    p1_list.append(player1_move) #.append ile p1liste hamle eklenir,
    
    player2_move=input( f'{player_2}:')   #oyuncu1 ile ayni islem yapilir,
    player2_move=player2_move.lower() 
    p2_list.append(player2_move) #.append ile p1liste hamle eklenir,
    
for i in range(game): #for... i range ile oyun sayisi i sira ile atanir,
        if p1_list[i]==p2_list[i]: # i. indexler karsiastirilir,
            player1_skor+=1 #esit ise 1 puan eklenir,
            player2_skor+=1
        elif p1_list[i]=='t' and p2_list[i]=='m': # i. indexler karsilastirilir oyuncu1 t oyuncu2 m ise, 
            player1_skor+=3                        #oyuncu1 e 3 puan eklenir,
        elif p1_list[i]=='t' and p2_list[i]=='k': # i. indexler karsilastirilir oyuncu1 t oyuncu2 m\k ise, 
            player2_skor+=3                         #oyuncu2 e 3 puan eklenir,
        elif p1_list[i]=='k'and p2_list[i]=='t':    
            player1_skor+=3
        elif p1_list[i]=='k'and p2_list[i]=='m':
            player2_skor+=3
        elif p1_list[i]=='m'and p2_list[i]=='k':
            player1_skor+=3
        elif p1_list[i]=='m'and p2_list[i]=='t':
            player2_skor+=1
             
        
if player1_skor==player2_skor: #skorlar esit cikar ise;
    print(f'{player_1}-{player_2}= {player1_skor}-{player2_skor} Berabere') #fstring ile {oyuncu1ad}-{oyuncu2ad}={oyuncu1skor}-{oyuncu2skor}
elif player1_skor>player2_skor: #oyuncu1 skor buyuk oyuncu2 ise;
    print(f'Oyun sonucu: {player_1}-{player_2} = {player1_skor}-{player2_skor}\n Tebrikler...{player_1}')
elif player1_skor<player2_skor:     #oyuncu1 skoru kucuk oyuncu 2 ise
    print(f'Oyun sonucu: {player_2}-{player_1} = {player2_skor}-{player1_skor}\n Tebrikler... {player_2}')
        
        
    

    # if player1_move==player2_move:#oyuncular ayni hamleyi yaptiklarinda her iksine de 1 er puan eklenir,
    #     player1_skor+=1
    #     player2_skor+=1
    # elif player1_move=='t' and player2_move=='m': #oyuncu 1 t>m oldugu icin 3 puan alir
    #     player1_skor+=3
    # elif player1_move=='t' and player2_move=='k': #oyuncu 2 k>t oldugu icin 3 puan alir,
    #     player2_skor+=3
    # elif player1_move=='m' and player2_move=='t': #oyuncu 2 t>m oldugu icin 3 puan alir,
    #     player2_skor+=3
    # elif player1_move=='m' and player2_move=='k': #oyuncu1 m>k oldugu icin 3 puan alir,
    #     player1_skor+=3
    # elif player1_move=='k' and player2_move=='t': #oyuncu1 k>m oldugu icin 3 puan alir,
    #     player1_skor+=3
    # elif player1_move=='k' and player2_move=='m': #oyuncu2 m>k oldugu icin 3 puan alir,
    #     player2_skor+=3
        

        
    
    
