
finansmanGelir=int(input("Finansman gelirinizi giriniz:"))
pazarGelir=int(input("Pazar gelirinizi giriniz:"))
kiraGelir=int(input("Kira gelirinizi giriniz:"))
def gelir(finansmanGelir,pazarGelir,kiraGelir):
    gelir=finansmanGelir+pazarGelir+kiraGelir
    print(gelir)
gelir(finansmanGelir,pazarGelir,kiraGelir)
ucret=int(input("Ücreti giriniz:"))
finansmanGider=int(input("Finansman giderinizi giriniz:"))
pazarGider=int(input("Pazar giderinizi giriniz:"))
kiraGider=int(input("Kira giderinizi giriniz:"))
muhasebeGider=int(input("Muhasebe giderinizi giriniz:"))
def gider(ucret,finansmanGider,pazarGider,kiraGider,muhasebeGider):
    gider=ucret+finansmanGider+pazarGider+kiraGider+muhasebeGider
    print(gider)
gider(ucret,finansmanGider,pazarGider,kiraGider,muhasebeGider)
gelir=int(input("İşletmenizin elde etttiği toplam geliri giriniz:"))
gider=int(input("İşletmenizin toplam giderlerini giriniz:"))
def kar(gelir,gider):
    kar=gelir-gider
    print(kar)
kar(gelir,gider)
kar=int(input("Elde ettiğiniz kar değerini giriniz:"))
if kar>1000:
    print("İşletmeniz kardadır.")
elif kar==1000:
    print("Kar yada zararınız yoktur.")
else:
    print("İşletmeniz zarardadır.")

print("kullanılabilirlik oranını hesaplama")
pus=int(input("planlamış üretim süresini giriniz:"))
pd=int(input("plansız duruş süresini giriniz:"))
def kullanılabilirlik (pus,pd):
    kullanılabilirlik=(pus-pd)/pus
    print(kullanılabilirlik)
kullanılabilirlik (pus,pd)
print("performans oranı hesaplama")
scz=int(input("standart cevrimiçi zamanı giriniz:"))
um=int(input("üretim miktarını giriniz:"))
def performans (scz,um,pus,pd):
    performans=(scz*um)/(pus-pd)
    print(performans)
performans (scz,um,pus,pd)
print("kalite oranını hesaplama")
sm=int(input("sağlam ürün miktarını giriniz:"))
tm=int(input("toplam üretim miktarını giriniz:"))
def kalite (sm,tm):
    kalite=sm/tm
    print(kalite)
kalite(sm,tm)
print("ekipman etkinlik oranı hesaplama")
def oee (pus,pd,scz,um,sm,tm):
    oee=((pus-pd)/pus)*((scz*um)/(pus-pd))*(sm/tm)*100
    print(oee)
oee(pus,pd,scz,um,sm,tm)


print("işletme cirosu hesaplama")
sm=int(input("satıs miktarınızı giriniz:"))
bsf=int(input("birim satıs fiyatınızı giriniz:"))
def ciro (sm,bsf):
    ciro=sm*bsf
    print(ciro)
ciro(sm,bsf)
print("adam bası ciro hesaplama")
tc=int(input("toplam ciro miktarınızı giriniz:"))
#tcs=toplam calisan sayisini ifade etmektedir.
tcs=25
def adambasiCiro(tc,tcs):
    adambasiCiro=tc/tcs
    print(adambasiCiro)
adambasiCiro(tc,tcs)
