#Check if the given two strings are 0 or 1 edits away
#Three types of edits -> insert a character, remove a character, replace a character

#Example
#agree -> agre, agrees, abree

#len(s1) == len(s2)
#len(s1) == len(s2) - 1 or len(s2) == len(s1) - 1

def edit_count(s1, s2):
	diff = abs(len(s1) - len(s2))

	if diff > 1:
		return False
	elif diff == 0:
		diff_count = 0
		for i in range(len(s1)):
			if s1[i] != s2[i]:
				diff_count += 1
				if diff_count > 1:
					return False
		return True
	else:
		if len(s1) > len(s2):
			bigger = s1
			smaller = s2
		elif len(s2) > len(s1):
			bigger = s2
			smaller = s1

		shift = 0

		for i in range(len(smaller)):
			#print(i), i = 0, 1, 2
			#shorter = ple
			#longer = pale
			if smaller[i] != bigger[i + shift]:
				if shift or (smaller[i] != bigger[i + 1]):
					return False
				shift = 1
			return True


	# l1 = list(s1)
	# l2 = list(s2)
	# l3 = [x for x in l1 if x not in l2]
	# if len(l3) == 0 or len(l3) == 1:
	# 	return True
	# else:
	# 	return False

# s1 = "pale"
# s2 = "ple"

# res = edit_count(s1, s2)

if __name__ == "__main__":
  import sys
  res = edit_count(sys.argv[-2], sys.argv[-1])
  print(res)



# s3 = s1.replace(s2, '')
# print(s3)

