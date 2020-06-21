#Rotate an NxN matrix by 90 degrees

#[[a, b, c],
# [d, e, f],  ==> Original NxN matrix
# [i, j, k],
#]

#Intermediate matrix
#[[i, j, k],
# [d, e, f], ==> Reversed NxN matrix
# [a, b, c]
#]

#Tranposed matrix of intermediate matrix -> rows become columns
#[[i, d, a],
# [j, e, b], ==> Rotated NxN matrix 
# [k, f, c]
#]

def rotate_by_90degrees(matrix):
	#matrix = matrix[::-1] ?
	matrix.reverse()
	for i in range(len(matrix)):
		for j in range(i):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	return matrix

# if __name__ == '__main__':
# 	import sys
# 	res_matrix = rotate_by_90degrees(sys.argv[-1])


matrix = [['a','b','c'],['d','e','f'],['i','j','k']]

res_matrix = rotate_by_90degrees(matrix)
print(res_matrix)



