import numpy as np

rng = np.random.default_rng(42)
array = rng.integers(1, 101, size=(3, 4, 5))
print("Array:\n", array)
print("Mean:", np.mean(array))
print("Median:", np.median(array))
print("Standard deviation:", np.std(array))
print("Variance:", np.var(array))
print("Minimum:", np.min(array))
print("Maximum:", np.max(array))
