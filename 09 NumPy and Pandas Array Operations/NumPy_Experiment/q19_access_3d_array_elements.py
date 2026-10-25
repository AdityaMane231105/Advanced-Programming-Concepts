import numpy as np

array = np.arange(1, 25).reshape(2, 3, 4)
print("First element:", array[0, 0, 0])
print("Last element:", array[-1, -1, -1])
print("Element at index [0, 1, 2]:", array[0, 1, 2])
print("Element at index [1, 2, 3]:", array[1, 2, 3])
