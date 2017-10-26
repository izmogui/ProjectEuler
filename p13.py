import argparse
import numpy
import time
import sys
import math

def main():
	
	parser = argparse.ArgumentParser()
	parser.add_argument("input_file")
	args = parser.parse_args()
	
	#millisec
	start = int(round(time.time() * 1000))

	
	original_matrix = numpy.genfromtxt(args.input_file, dtype="str", delimiter="\n")
	
	length = original_matrix.size/10
	if length == 0:
		digits_per_member = len(str(sys.maxint)) - 1
	else:
		digits_per_member = len(str(sys.maxint)) - length     
	# print (sys.maxsize)

	print "Chunk Digits: ", digits_per_member

	parcial_sum = 0

	print "Members: ", len(original_matrix[0])

	rounds = int(len(original_matrix[0])/digits_per_member) + 1
	first = 0
	last = 0
	partial_sum = 0
	partial_results = [0] * (rounds)

	#print(partial_results[0])

	print "Rounds: ", (rounds) 
	for i in range(0, rounds):	
		first = len(original_matrix[0]) - (digits_per_member * (i+1))
		last = len(original_matrix[0]) - (digits_per_member * i)
		if first < 0:
			first = 0
		for j in range(0, original_matrix.size):
			#print "\tPos [", first, "][", last, "]"
			#print "\t", original_matrix[j][first:last]
			partial_sum += int(original_matrix[j][first:last])

		carry = int (partial_sum / math.pow(10, digits_per_member))
		#print "Partial Sum = ", partial_sum, "index = ", rounds - i - 1, "partial_result = ", partial_sum - carry * math.pow(10, digits_per_member)
		if first == 0:
			partial_results[rounds - i - 1] = partial_sum
		else:
                        carry = int (partial_sum / math.pow(10, digits_per_member))
                        partial_results[rounds - i - 1] = int(partial_sum - carry * math.pow(10, digits_per_member))
                        partial_sum = carry
                        #print "Carry = ", partial_sum
		
	
	print partial_results	

	print "Elapsed Time: ", int(round(time.time() * 1000)) - start, "milliseconds"

if __name__ == "__main__":
    main()
