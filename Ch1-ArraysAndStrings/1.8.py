#If an element in an MxN matrix is 0, its entire row and column are set to 0

#[[1, 0, 5],
# [2, 9, 8], ==> Original MxN matrix
# [0, 6, 7]
#]

#[[0, 0, 0],
# [0, 0, 8], ==> Final MxN matrix
# [0, 0, 0]
#]

#INCOMPLETE
#Refer to
#https://github.com/w-hat/ctci-solutions/blob/master/ch-01-arrays-and-strings/08-zero-matrix.py

def zero_matrix(matrix):
	row_has_zero = False
	col_has_zero = False

	#Check if first row has a zero

	for j in range(len(matrix[0])):
		if matrix[0][j] == 0:
			row_has_zero = True
			break

	#Check if first column has a zero

	for i in range(len(matrix)):
		if matrix[i][0] == 0:
			col_has_zero = True
			break


	for i in range(len(matrix)):
		for j in range(len(matrix[0]):
			if matrix[i][j] == 0:
				matrix[i][0] = 0
				matrix[0][j] = 0


