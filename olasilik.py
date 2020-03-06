#1 den 20 ye kadar olan sayılardan asal olma olasılığı
from sympy import FiniteSet
from checkprime import check_prime
def probality(space,event):
    return len(event)/len(space)
space = FiniteSet(*range(1,21))
primes = []
for num in space:
    if check_prime(num):
        primes.append(num)
    event = FiniteSet(*primes)
p=probality(space,event)
print(p)
