import numpy as np

rng = np.random.default_rng(42)
array = rng.integers(1, 101, size=(2, 3, 4))
print("Original array:\n", array)
array[array > 50] = 0
print("Updated array:\n", array)
