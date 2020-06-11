#Check is one string is a permutation of another

import timeit

def permLists(s1, s2):
	l1, l2 = [], []
	if len(s1) != len(s2):
	 	return False
	for i in range(len(s1)):
		l1.append(s1.count(s1[i]))
		l2.append(s2.count(s2[i]))
		
	return sorted(l1) == sorted(l2)
	
def permSortedStrings(s1, s2):
	return sorted(s1) == sorted(s2)

def permCount(s1, s2):
	return all(s1.count(char) == s2.count(char) for char in s1)

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

#res = perm(s1, s2)
#print(res)

print(timeit.timeit(permLists, number=100000))
print(timeit.timeit(permSortedStrings, number=100000))
print(timeit.timeit(permCount, number=100000))


#https://stackoverflow.com/questions/396421/checking-if-two-strings-are-permutations-of-each-other-in-python



