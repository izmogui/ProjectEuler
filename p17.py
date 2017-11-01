import time

# Solution saving partial results.
# Bad performance to dictionary insertions and queries.
# Best known solution: brute froce without storing anything.

def main():
	
	#millisec
	start = int(round(time.time() * 1000))

	# top <= 20999
	top = 20999
	letters = 0
	values = dict()

	values[1] = 3
        values[2] = 3
        values[3] = 5
        values[4] = 4
        values[5] = 4
        values[6] = 3
        values[7] = 5
        values[8] = 5
        values[9] = 4
        values[10] = 3
        values[11] = 6
        values[12] = 6
        values[13] = 8
        values[14] = 8
        values[15] = 7
        values[16] = 7
        values[17] = 9
        values[18] = 8
        values[19] = 8
        values[20] = 6
        values[30] = 6
        values[40] = 5
        values[50] = 5
        values[60] = 5
        values[70] = 7
        values[80] = 6
        values[90] = 6
        values[100] = 7
        values[1000] = 8


        # case thousands
        thousands = top / 1000
	# get module
	thousands_module = top % 1000

	if thousands > 0:
		# first ($thousands - 1) rounds will repeat 1000 times the string (example: in case $top = 2000, the string "one thousand" will be repeated 1000 times)
		for i in range(1, thousands):
			letters += (values[i] + values[1000]) * 1000
		# The round $thousands will repeat ($thousands_module + 1) times the string (example: in case $top = 1200, the string "one thousand" will be repeated 200 + 1 times)
		letters += (values[thousands] + values[1000]) * (thousands_module + 1)


	# case hundreds
	if thousands > 0:
                # first ($thousands - 1) rounds will repeat 1000 times the string (example: in case $top = 2000, the string "one thousand" will be repeated 1000 times)
		for i in range(1, 10):
			letters += (values[i] + values[100]) * 100 * thousands
	
	extra_hundreds = thousands_module / 100
	extra_hundreds_module = thousands_module % 100
        if extra_hundreds > 0:
                # first ($thousands - 1) rounds will repeat 1000 times the string (example: in case $top = 2000, the string "one thousand" will be repeated 1000 times)
                for i in range(1, extra_hundreds):
                        letters += (values[i] + values[100]) * 100
                # The round $thousands will repeat ($thousands_module + 1) times the string (example: in case $top = 1200, the string "one thousand" will be repeated 200 + 1 times)
                letters += (values[extra_hundreds] + values[100]) * (extra_hundreds_module + 1)

	
	# case tens (20 ... 99)

	# case 0 + (1 ... 19)

	print letters

	print "Elapsed Time: ", int(round(time.time() * 1000)) - start, "milliseconds"

if __name__ == "__main__":
    main()
