from math import factorial, sqrt, e, exp

# e through limit definition
def limit_e(n):
	return (1+1/n)**n

# Taylor series for e^x.
def e_taylor(n, x):
	summa = 0
	for i in range (n+1):
		summa += 1/factorial(i)
	return summa

e_taylor = e_taylor(10, 1)
limit_e = limit_e(1000000)

print('\n\n')
print("Approximation to e^1 using a Taylor series with 10 sum elements:", e_taylor, '\n', 
	"Error of this approximation is:", abs(e_taylor - e), '\n')

print("Approximation to e using limit definition using n = 1 000 000:", limit_e, '\n',
	"Error of this approximation is:", abs(limit_e - e))
print('\n\n')
