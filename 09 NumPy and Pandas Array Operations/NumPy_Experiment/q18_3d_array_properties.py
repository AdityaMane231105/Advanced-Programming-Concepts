import numpy as np

array = np.arange(1, 25).reshape(2, 3, 4)
print("3D array:\n", array)
print("Number of dimensions:", array.ndim)
print("Shape:", array.shape)
print("Size:", array.size)
