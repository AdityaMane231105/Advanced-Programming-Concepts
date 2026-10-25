import numpy as np

array = np.array([10, 20, 30, 40])
array_with_label = np.append(array.astype(str), "Marks")
print("Original array:", array)
print("Array with character label:", array_with_label)
