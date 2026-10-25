import numpy as np

array = np.array([12, 67, 45, 89, 34, 51, 7, 100, 50, 73])
array[array > 50] = 0
print("Updated array:", array)
