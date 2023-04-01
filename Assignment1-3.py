import numpy as np
from numpy import sqrt

Matrix_A = np.ones((100, 100), dtype = int)
print(Matrix_A)
for i in range(100):
    for j in range(100):
        if i == j:
            Matrix_A[i][j] = j + 1

print(Matrix_A)


def frobenius_norm(mat):
    # To store the sum of squares of the
    # elements of the given matrix
    sum_of_square = 0
    row = 100
    col = 100
    for a in range(row):
        for b in range(col):
            sum_of_square += pow(abs(mat[a][b]), 2)

    # Return the square root of
    # the sum of squares
    res = sqrt(sum_of_square)
    return res


Frobenius_Norm = frobenius_norm(Matrix_A)
print("Frobenius norm of matrix: ", Frobenius_Norm)

