import sys
from operator import mul
import time


def main():
	
	
	#millisec
	start = int(round(time.time() * 1000))
	
	#foo
	
	print "Elapsed Time: ", int(round(time.time() * 1000)) - start, "milliseconds"

if __name__ == "__main__":
    main()
