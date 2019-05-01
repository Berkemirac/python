sayi = int(input("Sayi giriniz :"))
i=1
toplam=0
while(i<sayi):
    if (sayi % i == 0):
        toplam += i      
    i+=1
if(toplam==sayi):
        print(sayi,"Mükemmel Sayı")
            
else :
        print(sayi,"cık")

input()