def bölen(sayi) :
    bolenler = []
    for i in range (1,sayi+1) :
        if ( sayi % i ==0) :
            bolenler.append(i)
    return bolenler

while True :
    sayi = input("Sayi gir :")
    if (sayi =="q"):
        print("Çıkış yapılıyor")
        break
    else :
        sayi = int(sayi)
        print(bölen(sayi))



    input()


