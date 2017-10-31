import time

def main():
	
	#millisec
	start = int(round(time.time() * 1000))
	
	exponent = 1000
	
	digits = [1]
	aux_sum = 0
	
	# rounds
	for i in range(0, exponent):	
		# in each round iterate over all cells
		for j in range (0, len(digits)):
			# cell = 2*cell + carry
			aux_sum = digits[j] + digits[j] + aux_sum
			# carry overflow
			if aux_sum > 9:
				digits[j] = aux_sum % 10
				# case carry overflows the list
				if len(digits) <= j + 1:
					# increment list size by 1 and set carry
					digits.append(1)
					aux_sum = 0
				else:
					# set carry for the next iteration
					aux_sum = 1
			else:
				digits[j] = aux_sum
				aux_sum = 0

	#print digits
	print "Sum: ", sum(digits)
	
	print "Elapsed Time: ", int(round(time.time() * 1000)) - start, "milliseconds"

if __name__ == "__main__":
    main()
