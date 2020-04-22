def minHeapify(liste,index):
    """
    Aldığı index parametresini sağ ve sol çocuğu ile karşılaştırarak üçünden en küçüğünü bulur ve gerekiyorsa yer değiştirir.Bu işlemi recursive olarak devam ettirir.

    :param liste: Heap listesi
    :param index: Heapify ın uygulanmaya başlanacağı index
    """
    sol,sag,uzunluk,enkucuk = 2*index+1,2*index+2,len(liste)-1,index
    if sol <= uzunluk and liste[index] > liste[sol]:
        enkucuk=sol
    if sag <= uzunluk and liste[enkucuk] > liste[sag]:
        enkucuk=sag
    if enkucuk!=index:
        liste[index],liste[enkucuk]=liste[enkucuk],liste[index]
        minHeapify(liste,enkucuk)

def minHeapYap(liste):
    """
    Heap listesinin en az 1 çocuğu olan en son indexinden başlayarak sırayla tüm elemanlara minHeapify uygular ve listeyi heap haline getirir.
    :param liste: Heap listesi
    """
    for i in reversed(range(len(liste)//2)):
        minHeapify(liste,i)

def heapSort(liste):
    """
    Parametre olarak yollanan listeyi heap yapısına çevirir kök ile son elemanı yer değiştir, son elemanı siraliListe ye ekler ve liste'den siler.Ardından minHeapify uygulayarak tekrar heap haline getirdiği listeye bu işlemi her elemanı için tekrarlayarak listeyi küçükten büyüğe siraliListe de sıralar ve return eder.
    :param liste: Sıralanacak liste
    """
    liste,siraliListe=liste.copy(),[]
    minHeapYap(liste)
    for k in range(len(liste)):
        liste[0],liste[-1]=liste[-1],liste[0]
        siraliListe.append(liste.pop())
        minHeapify(liste,0)
    return siraliListe


##################################


def insertItemToHeap(myheap_1,item):
    """
    İlk parametredeki heap yapısına eleman ekler ve tekrar heap haline getirmek için minHeapYap fonksiyonunu uygular.Eleman varsa tekrar eklemez.
    :param myheap_1: Heap listesi
    :param item: Eklenecek değer.
    """
    if(not myheap_1.count(item)):
        myheap_1.append(item)
        minHeapYap(myheap_1)

def removeItemFrom(myheap_1):
    """
    Parametre olarak yollanan heap yapısının kökündeki eleman ile sondaki elemanı yer değiştirerek kökü yani en küçük elemanı heap yapısından kaldırır ve tekrar heap yapısına çevirmek için minHeapYap fonksiyonunu uygular.
    :param myheap_1: Heap listesi
    """
    if(len(myheap_1)):
        myheap_1[0],myheap_1[-1]=myheap_1[-1],myheap_1[0]
        myheap_1.pop()
        minHeapYap(myheap_1)


##################################

liste = [8,10,3,4,7,15,1,2,16]
minHeapYap(liste)
print(liste)
insertItemToHeap(liste,17)
removeItemFrom(liste)
removeItemFrom(liste)
removeItemFrom(liste)
print(heapSort(liste))
print(liste)
