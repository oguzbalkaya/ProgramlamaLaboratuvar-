from sympy import Symbol,Limit,sqrt,pi,Integral,pprint,exp
## Limit tanımından türev bulma
t,t1=Symbol('t'),Symbol('t1')
St=5*t**2+2*t+8
delta_t,St1 = Symbol('delta_t'),St.subs({t:t1})
St1_delta=St.subs({t:t1+delta_t})
pprint(Limit((St1_delta-St1)/delta_t,delta_t,0).doit())
##İntegral örneği
x = Symbol('x')
p = exp(-(x-10)**2/2) / sqrt(2*pi)
pprint(Integral(p,(x,11,12)).doit().evalf())