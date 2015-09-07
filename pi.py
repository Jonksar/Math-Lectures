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
# http://en.wikipedia.org/wiki/Riemann_zeta_function#Specific_values
# Show Euler derivation of this! It is awesome! Also known as Basel problem.
def zeta_function(z, n):
    summa = 0
    for i in range(1, n+1):
        summa += 1/i**z

    return summa

# riemann sum of half circle equation of radius 1 is equal to pi/2, after solving for y in 
# y^2 + x^2 = 1 (radius squared)
# http://en.wikipedia.org/wiki/Riemann_sum
# http://en.wikipedia.org/wiki/List_of_formulae_involving_%CF%80#Integrals
def riemann_sum(a, b, n):
    def f(x):   return sqrt(1-x**2)

    summa = 0
    i = a
    width = float((b - a)/n)
    while i <= b:
        summa += f(i) * width
        i += width

    return summa


pi_over_two = riemann_sum(-1, 1, 1000000)
print("\n\nNumerical calculation of integral under half circle with 1 000 000 rectangles:", pi_over_two, '\n',
	"Gives us pi of value:", pi_over_two * 2, "with error:", abs(pi_over_two * 2 - pi), '\n')


zeta_of_2 = zeta_function(2, 1000)
print("Numerical calculation of zeta(2) with 1000 sum elements, gives value of pi^2/6:", zeta_of_2, '\n',
	"Gives us value of pi:", sqrt(zeta_of_2 * 6), "with error of:", abs(pi - sqrt(zeta_of_2 * 6)), '\n')

arctan_1 = arctan(1, 100000)
print("Arctan Taylor series evaluated at 1 with 100 000 sum elements gives us value of", arctan_1, '\n'
	"Gives us pi value of:", arctan_1 * 4, "with error of:", abs(arctan_1 * 4 - Decimal(pi)), '\n')
print("Error is due to VERY slow convergance\n\n")
