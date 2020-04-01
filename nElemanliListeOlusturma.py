#min ve max arasındaki tam sayılardan oluşan n elemanlı bir liste oluşturur.
from random import randint as rand
def listeOlustur(n=10,min=1,max=100):
    liste = []
    for i in range(n):
        liste.append(rand(min,max))
    return liste
