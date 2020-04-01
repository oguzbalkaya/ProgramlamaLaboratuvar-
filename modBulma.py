histogram_liste = [[1, 4], [5, 2], [2, 1], [3, 6]]
histogram_sozluk= {1:4,5:2,2:1,3:6}
#Histogram liste ile oluşturulduysa
def modBul_liste(histogram):
    mod=histogram[0]
    for eleman in histogram:
        if eleman[1] > mod[1]:
            mod=eleman
    return mod[0]
#Histogram sözlük ile oluşturulduysa
def modBul_sozluk(histogram):
    modkey = -1
    mod = 0
    for eleman in histogram:
        if histogram[eleman] > mod:
            mod,modkey=histogram[eleman],eleman
    return modkey
print(histogram_sozluk)
print(histogram_liste)
print(modBul_sozluk(histogram_sozluk))
print(modBul_liste(histogram_liste))
