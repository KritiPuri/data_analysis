import numpy as np

#array using numpy 1d array
arr1 = np.array([1,3,5,7,9])
print(arr1)
print(type(arr1))
print(arr1.shape)

# 1d array
arr2 = np.array([2,4,5,6,7])
arr2.reshape(1,5) # 1 row 5 column

print(arr2)
# 2d array
arr2 = np.array([[1,2,3,4,5],[7,6,5,4,3]])
print(arr2)
print(arr2.shape) # 2 row 5 column

print(np.arange(0,10,2).reshape(5,1))
# This creates an array from 0 to 10 (exclusive) with step 2: [0,2,4,6,8]
# Then reshapes it into a 2D array with 5 rows and 1 column
# Output:
# [[0]
#  [2]
#  [4]
#  [6]
#  [8]]

print(np.ones((3,4))) # 3 row 4 column of ones
print(np.zeros((2,3))) # 2 row 3 column of zeros

#identity matrix
print(np.eye(4)) # 4*4 identity matrix

## Attributes of Numpy Array
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array:\n", arr3)
print("Shape of array:", arr3.shape)
print("data type",arr3.dtype)
print("dimensions",arr3.ndim) # ndim is used for dimensions
print("size of array:",arr3.size) # size is used for total number of elements
print("item size",arr3.itemsize)

### Numpy Vectorized Operation
arr1=np.array([1,2,3,4,5])
arr2=np.array([10,20,30,40,50])

### Element Wise addition
print("Addition:", arr1+arr2)

## Element Wise Substraction
print("Substraction:", arr1-arr2)

# Element-wise multiplication
print("Multiplication:", arr1 * arr2)

# Element-wise division
print("Division:", arr1 / arr2)
