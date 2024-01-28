import numpy as np

# Create a NumPy ndarray Object
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.
# NumPy ndarray object by using the array() function.

# 1-D Arrays
arr1 = np.array([1, 2, 3, 4])

print(f"Get the first element from 1-dimensional array:{arr1[0]}")

# 2-D Arrays
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Get 2-dimensional Arrays:{arr2}")

# 3-D Arrays
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(f"Get 3-dimensional Arrays:{arr3}")

# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

a = np.array(50)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Arrays
# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin argument.

arr4 = np.array([1, 2, 3, 4], ndmin=3)

print(f'Higher Dimensional Arrays: {arr4}')
print('number of dimensions :', arr4.ndim)