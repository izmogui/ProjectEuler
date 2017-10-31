import time

# Solution using permutations with repetition.
# There are always $rows + $columns movements, the problem is to obtain the number of possible orders.
# Permutation of ($rows + $columns) objects with $rows identical objects of type 1 and $columns identical objects of type 2.
# PR = (40!)/(20!*20!)

# Best Known Solution: this one

# recursive factorial
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

	print fact(rows + columns) / fact(rows) / fact(columns)
	
	print "Elapsed Time: ", int(round(time.time() * 1000)) - start, "milliseconds"

if __name__ == "__main__":
    main()
