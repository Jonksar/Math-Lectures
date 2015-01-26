from math import pi, factorial, sqrt
from decimal import Decimal, getcontext
getcontext().prec = 28

# Taylor series for arctan 1 = pi/4, fails due to limited precision and slow convergance
def arctan(x, n):
    summa = 0
    for i in range(0, n+1):
        summa += Decimal(((-1)**n)*((x)**(2*n+1))/(2*n+1))

    return summa

# zeta(2) = pi/6
def zeta_function(z, n):
    summa = 0
    for i in range(1, n+1):
        summa += 1/i**z

    return summa

# riemann sum of half circle equation of radius 1 is equal to pi/2
def riemann_sum(a, b, n):
    def f(x):   return sqrt(1-x**2)

    summa = 0
    i = a
    width = float((b - a)/n)
    while i <= b:
        summa += f(i) * width
        i += width

    return summa

#print(riemann_sum(-1 ,1, 1000000), pi/2)
print(zeta_function(2, 1000), pi**2/6)
#print(arctan(1,100000), pi/4)
