"""
<JHOMAR CANUMAY>
<8am-10:30am>
Create a python that would multiply two(2) integer matrix
requirement , row of the 1st of the matrix should have the same
size of the column of the 2nd matrix.
Result should be displayed in matrix similar to the multiplication table activity
matrix A(rxc)       matrix B(rxc)
1 2 3                   5 4 3
4 5 6                   1 2 6
7 8 9                   7 9 8
https://www.mathsisfun.com/algebra/matrix-multiplying.html
"""
from os import system
def main()->None:

	X = [[1,2,3],
		[4 ,5,6],
		[7 ,8,9]]
	
	Y = [[5,4,3],
		[1,2,6],
		[7,9,8]]
		
	result = [[0,0,0],
			[0,0,0],
			[0,0,0]]
		
	for i in range(len(X)):
		for j in range(len(Y[0])):
			for k in range(len(Y)):
				result[i][j] += X[i][k] * Y[k][j]
	
	for r in result:
		print(r)	
		
if __name__=="__main__":
	main()