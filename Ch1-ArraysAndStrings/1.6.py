#String compression
#if len(compressed_string) >= len(actual_string)
	#return actual_string
#else
	#return compressed_string

#bananahammock
#b1a4n2h1m2o1c1k1 -> return bananahammock

#cravingbuttercookies
#c2r2a1i2n1g1b1u1t2e2 -> stop at this point and return cravingbuttercookies, break loop

def string_compress(actual_string):
	freq = {}

	for i in actual_string:
		if i in freq:
			freq[i] += 1
		else:
			freq[i] = 1

	compressed_string = ""

	for char, count in freq.items():
		compressed_string += char + str(count)

	if len(compressed_string) > len(actual_string):
		return actual_string
	else:
		return compressed_string


if __name__ == "__main__":
	import sys
	res_string = string_compress(sys.argv[-1])
	print(res_string)

#List solution instead of dictionary 
#https://github.com/w-hat/ctci-solutions/blob/master/ch-01-arrays-and-strings/06-string-compression.py