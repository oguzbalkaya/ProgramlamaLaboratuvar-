"""
Başarılı olma olasılığı -> p = 0.58
Toplam gerçekleşecek olay sayısı -> n = 40
Başarılı olarak gerçekleşmesini istediğimiz olay sayısı -> k = 10

Başarılı olma olasılığı p=0.58 olan bir olayın n=40 kez gerçekleştiğinde k=10 kez başarılı olma olasılığının binom dağılım grafiği.


Oğuz BALKAYA 170401045
"""
from sympy import * #sympy kütüphanesi
import matplotlib.pyplot as plt
x,n,p,k = Symbol('x'),Symbol('n'),Symbol('p'),Symbol('k')
f = binomial(n,k) * p ** k * (1-p)**(n-k)
## SymPy kütüphanesi ile ##
plot(f.subs({p:0.58,k:10}),(n,1,40),title="Binomial Distribution Graph")
## for ve klasik matplotlib.pyplot kütüphanesi ile ##
xDegerleri,yDegerleri=[],[]
for i in range(1,40):
    y = f.subs({p:0.58,k:10,n:i})
    xDegerleri.append(i)
    yDegerleri.append(y)
plt.plot(xDegerleri,yDegerleri)
plt.show()
