import time

# Solution storing partial results.
# Bad performance due to dictionary insertions and queries.
# Best known solution: brute froce without storing anything.

def main():
	
	#millisec
	start = int(round(time.time() * 1000))
	
	top = 1000000
	value = 0
	max_key = 0
	max_value = 0
	key_value = dict()

	# base case
	key_value[1] = 1
	
	for i in range(1, top):
		value = i
		sequence = dict()
		while True:
			# case saved value
                        if value in key_value:
				# move from partial to global hashtable
				for key in sequence:
					key_value[key] = sequence[key] + key_value[value]
				break
			else:
				# increment size of each partial value
				for key in sequence:
					sequence[key] += 1
				
				# save only values below top value. (Most values that are above will only be queried once)
				if value <= top:
					sequence[value] = 1
				
				# operation depending even/odd
				if value % 2 != 0:
					value = 3 * value + 1
				else:
					value = value / 2
	
	# calculate maximum
	for i in range(1, top):
		if key_value[i] > max_value:
			max_key = i
			max_value = key_value[i]
	
	print "[ key, value ]: [", max_key, ", ", max_value, "]"

	print "Elapsed Time: ", int(round(time.time() * 1000)) - start, "milliseconds"

if __name__ == "__main__":
    main()
