# import numpy as np
# arr=np.array([1,2,3,4,5])
# x=arr.copy()
# arr[0]=55
# print(x)
# print(arr)


import numpy as np
arr=np.array([2,3,4,5,6])
x=arr.view()
arr[1]=60
print(x)
print(arr)