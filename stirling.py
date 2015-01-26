from math import factorial, sqrt, pi, e
# Using stirling approximation approximate factorial function. Very accurate after n > 1000
# http://en.wikipedia.org/wiki/Stirling%27s_approximation


def stirling(t):
	return sqrt(2*pi*t)*(t/e)**t
	
print(stirling(100), factorial(100)*1.0)
