import numpy as np

matrix1 = np.arange(1, 10).reshape(3, 3)
matrix2 = np.arange(9, 0, -1).reshape(3, 3)
print("First matrix:\n", matrix1)
print("Second matrix:\n", matrix2)
print("Matrix addition:\n", matrix1 + matrix2)
