#1.SORU
satisMik=500
birimSatisF=20
ciro=5000
i=0
while(ciro<=500000):
    ciro=ciro+(satisMik*birimSatisF)
    satisMik=satisMik+200
    birimSatisF=birimSatisF+10
    i=i+1
print("500000 den fazla kar",i,"ayda tamamlanmıştır,")
    

#2.SORU
sm=10000
satılanurun=500
alınanurun=100
i=0
while True:
    sm=sm-satılanurun+alınanurun
    i=i+1
    if(sm==0):
        print(i,"ay sonra stok miktarı sıfırdır.")
        break


#3.SORU
print("3 sayısının bölümünden kalan sayıların toplamı")
print("Çıkış yapmak istiyorsanız 0 sayısını giriniz")
kalanlar = 0
while True:
    sayi = int(input("Sayı Giriniz : "))
    if(sayi > 0 ):
        kalanlar = kalanlar+(sayi%3)
        print("Girilen Sayıların 3 ile bölümünden kalanların toplamı =",kalanlar)
    else:
        break     
        

#4.SORU
gunluky=90
calisansayisi=50
mesaisaati=""
calismasaati=40
while True:
    mesaisaati=int(input("mesai saatinizi giriniz:"))
    if (mesaisaati<22):
        print("aylık mesai ile birlikte ödenecek miktar:",(40*4*90)+(mesaisaati*gunluky*0.10))
    else:
        print("22 saatten fazla mesai yapılmaz.")
        break


#5.SORU
gunlukurun=200
defolumal=""
toplamdefo=0
i=0
while True:
    defolumal=int(input("Günlük defolu ürün sayısınız giriniz:"))
    toplamdefo=toplamdefo+defolumal
    i=i+1
    print(i,"günlük toplam defolu ürün sayınız:",toplamdefo)
    if(defolumal>(gunlukurun*0.20)):
        print("Defolu ürün sayınız günlük mal üretiminizin %20'nin üzerindedir")
        
