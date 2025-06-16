import numpy as np

arr = np.array([1, 2, 3, 4])
arr_5d = arr.reshape(1, 1, 1, 2, 2)
print(arr_5d)
print("Dimensions:", arr_5d.ndim)
