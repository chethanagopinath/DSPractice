#Check if a string has all unique characters
#No additional data structures

def checkUniqueness(string):
	for i in string:
		if string.count(i) > 1:
			return False
	return True

unique = checkUniqueness("hello")
print(unique)