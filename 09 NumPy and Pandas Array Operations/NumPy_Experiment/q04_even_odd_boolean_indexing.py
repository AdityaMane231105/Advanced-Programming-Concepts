import numpy as np

array = np.arange(1, 21)
print("Even numbers:", array[array % 2 == 0])
print("Odd numbers:", array[array % 2 != 0])
