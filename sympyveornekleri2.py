import sympy as sym
import sympy.plotting as syp
import matplotlib.pyplot as plt
sym.init_printing()
sigma,mu,x = sym.Symbol('sigma'),sym.Symbol('mu'),sym.Symbol('x')
sym.pprint(2*sym.pi*sigma)
part1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
part2 = sym.exp(-1*((x-mu)**2)/(2*sigma**2))
gauss_function=part1*part2
sym.pprint(gauss_function)
sym.plot(gauss_function.subs({mu:0,sigma:1}),(x,-10,10),title="Gauss")

###Aynı işlemi for döngüsü ile yapalım.
#evalf() -> matematiksel hale getirir.
x_values,y_values = [],[]
for value in range(-10,10):
    y = gauss_function.subs({mu:1,sigma:1,x:value}).evalf()
    x_values.append(value)
    y_values.append(y)
plt.plot(x_values,y_values)
plt.show()