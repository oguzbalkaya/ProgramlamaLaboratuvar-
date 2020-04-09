from sympy import *
x = Symbol('x') #Sembol olarak değişkene değer atıyoruz.
fonksiyon = x+x+1
pprint(fonksiyon) #Çıktıyı matematiksel olarak veriyor.Örneğin 2*x+1 i 2.x+1 olarak veriyor.
###
x,y = Symbol('x'),Symbol('y')
p = x*(x+x)
pprint(p)
p *= (x+2)*(x+3)
pprint(p)
###
expr = x**2 - y**2
pprint(factor(expr)) #Çarpanlarına ayırır
pprint(expand(factor(expr))) #Çarpanlarına ayrılmış veriyi açar.
#Örnek
expr = x**3+3*x**2*y+3*x*y**2+y**3
factors=factor(expr)
pprint(factors)
pprint(expand(factors))
###
def seriOlustur(n):
    series = x
    for i in range(2,n+1):
        series += (x**i)/i
    return series
pprint(seriOlustur(int(input("Bir sayı girin : "))))
###
expr = x*x+x*y+x*y+y*y
res = expr.subs({x:1,y:2}) #subs ile değişkenlere değer verdik
print(res)
res=expr.subs(x,1-y) #tüm ifadeyi y cinsine çevirdik.
pprint(res)