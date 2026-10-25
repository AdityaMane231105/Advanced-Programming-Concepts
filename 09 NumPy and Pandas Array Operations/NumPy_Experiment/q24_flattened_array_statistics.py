import numpy as np

array = np.arange(1, 28).reshape(3, 3, 3)
flat_array = array.flatten()
print("Flattened array:", flat_array)
print("Sum:", np.sum(flat_array))
print("Average:", np.mean(flat_array))
print("Maximum:", np.max(flat_array))
print("Minimum:", np.min(flat_array))
