#Listede bulunan elemanların kaçar tane olduğunu bulan fonksiyon
def my_h(list_1):
    dict_1=dict()
    for i in list_1:
        if i in dict_1:
            dict_1[i]+=1
        else:
            dict_1[i]=1
    return dict_1
list1=[0,5,25,100,5,5,0,100]
print(my_h(list1))
