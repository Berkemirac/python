from math import *

print("""************************
Gelişmiş Hesap Makinesi
******************""")

print("""Yapmak istediğiniz işlemi seçin:
1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
5.Karekök alma
6.Kare alma
7.Faktöriyel alma
8.Radyandan dereceye çevirme
9.Dereceden radyana çevirme
10.Sin değeri
11.Cos değeri
12.Tan değeri
13.Cot değeri
""")


while True :
    islem=int(input("İşlemi seç :"))
    if(islem==1) :
        a = int(input("Sayi giriniz:"))
        b = int(input("Sayi giriniz:"))
        print("{} ile {} nin toplami {}'dir".format(a,b,a+b))
    elif(islem==2) :
        a = int(input("Sayi giriniz:"))
        b = int(input("Sayi giriniz:"))
        print("{} ile {} nin çıkarması {}'dir".format(a,b,a-b))
    elif(islem==3) :
        a = int(input("Sayi giriniz:"))
        b = int(input("Sayi giriniz:"))
        print("{} ile {} nin çarpımı {}'dir".format(a,b,a*b))
    elif(islem==4) :
        a = int(input("Sayi giriniz:"))
        b = int(input("Sayi giriniz:"))
        print("{} ile {} nin bölümü {}'dir".format(a,b,a/b))
    elif(islem==5) :
        a = int(input("Sayi giriniz:"))
        print(sqrt(a))
    elif(islem==6) :
        a = int(input("Sayi giriniz:"))
        print(a**2)
    elif(islem==7) :
        a = int(input("Sayi giriniz:"))
        print(factorial(a))
    elif(islem==8) :
        a = int(input("Radyan giriniz:"))
        print(degrees(a))
    elif(islem==9) :
        a = int(input("Derece giriniz:"))
        print(radians(a))
    elif(islem==10) :
        a = int(input("Derece giriniz:"))
        print(sin(radians(a)))
    elif(islem==11) :
        a = int(input("Derece giriniz:"))
        print(cos(radians(a)))
    elif(islem==12) :
        a = int(input("Derece giriniz:"))
        print(tan(radians(a)))
    elif(islem==13) :
        a = int(input("Derece giriniz:"))
        print(cos(radians(a)) / sin(radians(a)))
    else :
        print("Geçersiz işlem")

# round deyimi********* 
# 2.667 =a diyelim
 # round(a) 3 olur
 # round(a,2) 2.67

input()
