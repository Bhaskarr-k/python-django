# x=[1,2,3,4]
# y=[6,7,8,9]
# z=[]
# for i,j in zip(x,y):
#     z.append(i+j)
# print(z)

import numpy as np
x=[1,2,3,4]
y=[6,7,8,9]
z=np.add(x,y)
print(z)