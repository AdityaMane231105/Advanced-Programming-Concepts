import numpy as np

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
print("Horizontal concatenation:\n", np.concatenate((array1, array2), axis=1))
print("Vertical concatenation:\n", np.concatenate((array1, array2), axis=0))
