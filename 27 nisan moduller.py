#1.soru:
def isletmeKari (x,y):
    x=int(x)
    y=int(y)
    isletmeKari=x-y
    print(isletmeKari)
def adambasiCiro (a,b):
    a=int(a)
    b=int(b)
    adambasiCiro=a/b
    print(adambasiCiro)

#2.soru:
class aktif:
    def hesapla(kasa,alınan,bankalar,alıcak,ticari,binalar,tasitlar,demirB):
        aktif=(kasa+alınan+bankalar+alıcak+ticari+binalar+tasitlar+demirB)
        return aktif
class pasif:
    def hesapla(banka,satıcılar,bankaK,borc,özS):
        pasif=(banka+satıcılar+bankaK+borc+özS)
        return pasif

#3.soru:
class etkilesim_orani:
    def __init__(self,begeni,yorum,paylasim,icerik,takip):
        etki=(((begeni+yorum+paylasim)/icerik)/takip)*100
        print(float(etki))
        if etki>=0.20:
           print("basarili")
        else:
            print("bsarısız")
