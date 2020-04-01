#Yollanan listedeki elemanların tekrar sayılarını bulur.
from nElemanliListeOlusturma import listeOlustur
liste = listeOlustur(10,1,5)
def histogramOlustur(liste):
    histogram = []
    for i in range(len(liste)):
        kontrol = False
        for k in range(len(histogram)):
            if(liste[i]==histogram[k][0]):
                histogram[k][1]+=1
                kontrol=True
        if kontrol == False:
            histogram.append([liste[i],1])
    return histogram
print(histogramOlustur(liste))
