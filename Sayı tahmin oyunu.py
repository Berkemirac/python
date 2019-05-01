import time
import random

print("""*********************************
    SAYI TAHMİN OYUNU (1-40 ARASI)
    ******************************""")
sallanan = random.randint(1,40)
hak = 1
while True :
    tahmin=int(input("Sayi giriniz:"))
    if(tahmin<sallanan):
        print("Kontrol ediliyor")
        time.sleep(1)
        print("Daha yüksek bir sayi söyleyin")
        hak-=1
    elif(tahmin>sallanan):
        print("Kontrol ediliyor")
        time.sleep(1)
        print("Daha düşük bir sayi söyleyin")
        hak-=1
    else :
        print("Kontrol ediliyor")
        time.sleep(1)
        print("Bildin...")
    if(hak==0):
        print("Hakkın bitti...")
        print("Sayi {} idi".format(sallanan))
        break

input()