import numpy as np

ar = np.array([1,2,3,0,4,5,6,7]) # ar is the ndarray object

ar2 =  np.array([
    [1,2,3],
    [4,5,6]
])
# print(ar.max())
print(ar[-2]) # 0, 1, 2, 3, 4, 5

for i in ar:
    print(i)