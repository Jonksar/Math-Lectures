from math import factorial, sqrt, pi, e
# Using stirling approximation approximate factorial function. Very accurate after n > 1000
# http://en.wikipedia.org/wiki/Stirling%27s_approximation


def stirling(t):
	return sqrt(2*pi*t)*(t/e)**t

s = stirling(100)
f = factorial(100) * 1.0
print("\n\nStirling approximation to 100! is:", s, "Compared to exact value of:", f, '\nThe error is:', f - s, "\nWhich is only:", ((f - s) / f) * 100, "%\n\n")
