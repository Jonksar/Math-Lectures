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


# First example problem?
def bacteria_growth(deltat, t, r, n):
	history = []
	time = 0
	while time < t:
		time += deltat
		history.append(1/(1+exp(-r*time/n)))
	
	return history


print(e_taylor(100, 1))
print(limit_e(1000))
print(bacteria_growth(1, 100, 1, 10000))
