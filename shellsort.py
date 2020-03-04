def shellSort(arr):
    n = len(arr)
    gap = n//2
    while gap>0:
        for i in range(gap,n):
            temp = arr[i]
            j=i
            while j>=gap and arr[j-gap]>temp:
                arr[j] = arr[j-gap]
                j=j-gap
            arr[j] = temp
        gap//=2

dizi = [23,10,12,6,5,18,1]
shellSort(dizi)
print(dizi)