import sys
from operator import mul
import time

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


	
	print "Elapsed Time: ", int(round(time.time() * 1000)) - start, "milliseconds"

if __name__ == "__main__":
    main()
