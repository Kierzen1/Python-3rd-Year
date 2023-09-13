"""
Kierzen Ivan Jay P. Booc
MW 8:00-10:30
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
    system("cls")
    matrixA:int = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
    matrixB:int = [[5, 4, 3],
                   [1, 2, 6],
                   [7, 9, 8]]
                   
    rows = len(matrixA)
    cols1 = len(matrixA[0])
    cols2 = len(matrixB[0])
    
    matrixResult = [[0 for c in range(cols2)] for r in range(rows)]
    
    for row in range(rows):
        for column in range(cols2):
            for result in range(cols1):
                matrixResult[row][column] += matrixA[row][result] * matrixB[result][column]

    for row in matrixResult:
        print(" ".join([f"{element:5}" for element in row]))

if __name__=="__main__":
    main()