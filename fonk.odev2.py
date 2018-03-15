#1.soru
print("katma deger ciro hesaplama")
tsm=int(input("toplam satis miktarinizi giriniz:"))
hm=int(input("hammadde maliyetinizi giriniz:"))
bog=int(input("bakim onarim maliyetinizi giriniz:"))
sg=int(input("sevkiyat giderlerinizi giriniz:"))
sahg=int(input("satin alinan hizmet giderlerinizi giriniz:"))
def kdc(tsm,hm,bog,sg,sahg):
    kdc=tsm-(hm+bog+sg+sahg)
    if (kdc)>1000:
        print("işletme katma değer cirosu yüksektir.")
    elif (kdc)<500:
        print("işletme katma değer cirosu düşüktür.")
    else:
        print("işletme katma değer cirosu normaldir.")
    print(kdc)
kdc(tsm,hm,bog,sg,sahg)



#2.soru
def mcs(cs,tms):
    global muscs
    muscs=cs/tms
    return muscs
def mcsü(cas,tmus):
    global mucasu
    mucasu=cas/tmus
    return mucasu
def fark(mucasu,muscs):
    calısmasurefark=mucasu-muscs
    print("çalışma süreleri arasındaki fark",calısmasurefark)
muscs=int(input("yılınızı giriniz"))
cs=int(input("calısan süresini giriniz:"))
tms=int(input("toplam musteri sayısını giriniz:"))
mucasu=int(input("farkını almak istediğiniz yılı giriniz:"))
cas=int(input("calısan süresini giriniz:"))
tmus=int(input("toplam musteri sayısını giriniz:"))
musterilerlecalismasuresi=mcs(cs,tms)
musterilerlecalismasuresii=mcsü(cas,tmus)
fark(musterilerlecalismasuresi,musterilerlecalismasuresii)




#3.SORU
print("ilk altı aylık gelir kalemleri")
yg=int(input("yazılım gelirinizi giriniz:"))
fg=int(input("finansman gelirinizi giriniz:"))
usg=int(input("ürün satış gelirinizi giriniz:"))
print("ilk altı aylık gider kalemleri")
cm=int(input("calısan maaslarını giriniz:"))
kg=int(input("kira gelirinizi giriniz:"))
dm=int(input("donanım maliyetlerinizi giriniz:"))
print("son altı aylık gelir kalemleri")
yage=int(input("yazılım gelirinizi giriniz"))
sg=int(input("sponsorluk gelirinizi giriniz:"))
eg=int(input("e ticaret gelirinizi giriniz:"))
usage=int(input("ürün satış gelirinizi giriniz:"))
print("son altı aylık gider kalemleri")
cama=int(input("calısan maaslarını giriniz:"))
kigi=int(input("kira giderinizi giriniz:"))
bm=int(input("bakım maliyetinizi giriniz:"))
def gelir(yg,fg,usg):
    global ilkGelir
    ilkGelir=yg+fg+usg
    return ilkGelir
def gider(cm,kg,dm):
    global ilkGider
    ilkGider=cm+kg+dm
    return ilkGider
def gelir2(yage,sg,eg,usage):
    global ikinciGelir
    ikinciGelir=yage+sg+eg+usage
    return ikinciGelir
def gider2(cama,kigi,bm):
    global ikinciGider
    ikinciGider=cama+kigi+bm
    return ikinciGider
def karHesapla(ilkGelir,ilkGider,ikinciGelir,ikinciGider):
    kar=(ilkGelir-ilkGider)-(ikinciGelir-ikinciGider)
    if (kar>5000):
        print("işletme çok karlı")
    elif (kar<1000):
        print("işletme yeterince karlı degil")
    else:
        print("işletme karı normal")
ilkGelirimiz=gelir(yg,fg,usg)
ilkGiderimiz=gider(cm,kg,dm)
ikinciGelirimiz=gelir2(yage,sg,eg,usage)
ikinciGiderimiz=gider2(cama,kigi,bm)
karHesapla(ilkGelirimiz,ilkGiderimiz,ikinciGelirimiz,ikinciGiderimiz)




#4.SORU
print("dönem sonu stok")
ks=int(input("koltuk sayınızı giriniz:"))
ys=int(input("yatak sayınızı giriniz:"))
ds=int(input("dolap sayınızı giriniz:"))
print("dönem bası stok")
ksa=int(input("koltuk sayınızı giriniz:"))
ysa=int(input("yatak sayınızı giriniz:"))
dsa=int(input("dolap sayınızı giriniz:"))
def dönemBasi(ks,ys,ds):
    global dönemBasiStok
    dönemBasiStok=ks+ys+ds
    return dönemBasiStok
def dönemSonu (ksa,ysa,dsa):
    global dönemSonuStok
    dönemSonuStok=ksa+ysa+dsa
    return dönemSonuStok
def ortalama(dönemSonuStok,dönemBasiStok):
    ortalamaStok=(dönemSonuStok+dönemBasiStok)/2
    print("ortalama stok miktarı",ortalamaStok)
dönemBasiStokMiktari=dönemBasi(ks,ys,ds)
dönemSonuStokMiktari=dönemSonu(ksa,ysa,dsa)
ortalama(dönemBasiStokMiktari,dönemSonuStokMiktari)
