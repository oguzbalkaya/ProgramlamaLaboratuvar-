#Listedeki elemanların ardışık sırada en yüksek toplamı
liste_1 = [4,-3,5,-2,-1,2,6,-2]
max_1=0
for i in range(len(liste_1)+1):
    for j in range(i,len(liste_1)+1):
        t=0
        for k in range(i,j):
            t=t+liste_1[k]
        if max_1<t:
            max_1=t
            i_1,i_2=i,j
print(max_1,i_1,i_2)


##

def my_f_1(list_1 = [4,-3,5,-2,-1,2,6,-2]):
    maxSum = 0
    n = len(list_1)
    for i in range(n):
        for j in range(i,n):
            t = 0
            for k in range(i,j):
                t+=list_1[k]
            if t>maxSum:
                maxSum = t
    return maxSum

##

def my_f_2(list_1 = [4,-3,5,-2,-1,2,6,-2]):
    maxSum = 0
    n = len(list_1)
    for i in range(n):
        t = 0
        for j in range(i,n):
            t+=list_1[j]
            if t>maxSum:
                maxSum = t
    return(maxSum)

print(my_f_2())


