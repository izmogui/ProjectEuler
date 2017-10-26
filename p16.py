import sys
from operator import mul
import time

def factorial(num):
    """Iteratively calculate num!."""
    return reduce(mul, xrange(1, num+1)) if num else 1

def fact(num):
	if num == 0 or num == 1:
		return 1
	else:
		return num * fact(num - 1)

def main():
	
	
	#millisec
	start = int(round(time.time() * 1000))
	
	rows = 20
	columns = 20

	print factorial(rows+columns)
	print fact (rows + columns)

	
	print "Elapsed Time: ", int(round(time.time() * 1000)) - start, "milliseconds"

if __name__ == "__main__":
    main()
