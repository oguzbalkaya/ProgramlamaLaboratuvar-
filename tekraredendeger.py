#Yollanan sözlükte(dict) yollanan değer(value) kadar tekrar eden değer varmı kontrol.

#Aynı tekrar sayısına sahip birden fazla değer varsa liste şeklinde hepsini döndürür. 
def lookup(dict,value):
    list = []
    for k in dict:
        if dict[k] == value:
            list.append(k)  
    return list  
dict1 = {0 : 5, 1 : 5 , 2 : 10 , 3: 15 , 4:20 , 5:15, 6 : 15}
print(lookup(dict1,15))

#İstenen değer kadar tekrar edilmiş ilk değeri döndürür.
def lookup2(dict,value):
    list = []
    for k in dict:
        if dict[k] == value:
            return k  #return k
    return -1
print(lookup2(dict1,15))


