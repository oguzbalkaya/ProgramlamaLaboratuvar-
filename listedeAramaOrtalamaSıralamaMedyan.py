def arama(liste,aranan):
    """Listede dolaşarak aranan değerini bulmaya çalışır.Eğer bulursa bulduğu indexi bulamazsa -1 i döndürür"""
    for i in range(len(liste)):
        if liste[i] == aranan:
            return i
    return -1
def ortalama(liste):
    """Listedeki sayıların aritmatik ortalamasını bulur."""
    toplam = 0
    for i in liste:
        toplam+=i
    return toplam/len(liste)
def bubbleSort(liste):
    """Listeyi küçükten büyüğe sıralar."""
    for i in range(len(liste)-1,-1,-1):
        for j in range(0,i):
            if not liste[j]<liste[j+1]:
                temp=liste[j]
                liste[j],liste[j+1]=liste[j+1],temp
    return liste
def binarySearch(liste,aranan):
    """Aranan listede varsa 1 yoksa 0 döndürür."""
    altSinir,ustSinir=0,len(liste)-1
    while altSinir<=ustSinir:
        orta = (altSinir+ustSinir)//2
        if liste[orta] == aranan:
            return 1
        elif liste[orta]>aranan:
            ustSinir=orta-1
        else:
            altSinir=orta+1
    return 0
def medyan(liste):
    if len(liste)%2==1:
        orta = int(len(liste)/2)+1
        print(orta)
        return liste[orta-1]
    else:
        orta1,orta2=liste[int(len(liste)/2)],liste[int(len(liste)/2)-1]
        print(orta1,orta2)
        return (orta1+orta2)/2
liste = [7,6,4,5,1,2,3,8]
print(bubbleSort(liste))
print(binarySearch(liste,8))
print(medyan(bubbleSort(liste)))
print(arama(liste,58),"Ortalama = ",ortalama(liste))
