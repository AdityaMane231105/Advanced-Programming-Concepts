import numpy as np

rng = np.random.default_rng(42)
array = rng.integers(1, 101, size=(3, 4, 5))
flat_array = array.flatten()
average = np.mean(flat_array)
print("3D array:\n", array)
print("Elements greater than 50:", flat_array[flat_array > 50])
print("Even numbers:", flat_array[flat_array % 2 == 0])
print("Average:", average)
print("Elements less than average:", flat_array[flat_array < average])
