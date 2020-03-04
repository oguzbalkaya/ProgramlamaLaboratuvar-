def insertionSort(arr):
    n = len(arr)
    for i in range(1,n): #Dizinin 0. elemanı başlangıçta sorted kısma denk geldiği için 1 den başladık.
        key = arr[i]
        j = i-1 #Sıralı kısmın son elemanı
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1]=key

dizi = [23,10,12,6,5,18,1]
insertionSort(dizi)
print(dizi)