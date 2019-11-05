# This programming example by Ale und Arben demonstrates software development with unit tests.

# programming of function was started with:
# def max3(a, b, c):
#	pass

def max3(a, b, c):
	if a > b and a > c:
		return a
	if b > c:
		return b
	return c

if max3(0, 0, 0) != 0: print('fail 0 0 0 ') # first unit test condition
if max3(1, 0, 0) != 1: print('fail 1 0 0 ')
if max3(0, 1, 0) != 1: print('fail 0 1 0 ')
if max3(0, 0, 1) != 1: print('fail 0 0 1 ')
if max3(3, 2, 4) != 4: print('fail 3 2 4 ')

# unit testing
# test driven development
