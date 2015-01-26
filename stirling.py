from math import factorial, sqrt, pi, e

def stirling(t):
	return sqrt(2*pi*t)*(t/e)**t
	
print(stirling(100), factorial(100)*1.0)
