kelimeler = []
def dosyaOku(dosyaAdi):
    return open(dosyaAdi,"r+",encoding="UTF-8",errors="ignore")
def histogramOlustur(girilen):
    histogram = dict()
    for dosyaNumarasi in range(1,11):
        for satir in dosyaOku("data_files/"+str(dosyaNumarasi)+".txt"):
            satir,girilen = satir.lower().strip(),girilen.lower().strip()
            ayir=satir.split()
            for k in ayir:
                kelimeler.append(k)
            if(girilen in satir):
                satir = satir.split(girilen)
                if len(satir) > 1:
                    for i in range(1, len(satir)):
                        satir[i] = satir[i].strip()
                        if (len(satir[i].split()) > 0):
                            if(satir[i].split()[0] in histogram):
                                histogram[satir[i].split()[0]]+=1
                            else:
                                histogram[satir[i].split()[0]] = 1
    return histogram
def kelimemi(girilen):
    girilen=girilen.split()
    for kelime in girilen:
        if kelime not in kelimeler:
            return 0
    return 1
def oneriYap(okunacakDosya,yazilacakDosya):
    dosyaOkunacak,dosyaYazilacak=dosyaOku(okunacakDosya),open(yazilacakDosya,"w+",encoding="UTF-8",errors="ignore")
    for kelime in dosyaOkunacak:
        if len(kelime.split()) <=5:
            kelime = kelime.replace("\n","")
            oneriler = histogramOlustur(kelime)
            if (kelimemi(kelime.lower())):
                print(oneriler)
                encokadet,encokstring=0," "
                for i in oneriler:
                    if oneriler[i] > encokadet:
                        encokadet,encokstring=oneriler[i],i
                dosyaYazilacak.write(kelime+" : "+encokstring+"\n")
            else:
                dosyaYazilacak.write(kelime+" : Öneri yok.\n")
        else:
            raise ValueError
    dosyaYazilacak.close()
    dosyaYazilacak.close()
try:
    oneriYap("data_files/input.txt","data_files/output.txt")
except ValueError:
    print("Öneri almak için maksimum 5 kelime girin.")