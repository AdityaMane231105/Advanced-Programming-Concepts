import numpy as np

array = np.arange(1, 25).reshape(2, 3, 4)
print("Sum of all elements:", np.sum(array))
print("Sum of each layer:", np.sum(array, axis=(1, 2)))
print("Sum along rows:\n", np.sum(array, axis=2))
print("Sum along columns:\n", np.sum(array, axis=1))
