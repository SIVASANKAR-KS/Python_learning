import numpy as np

def print_with_lines(title):
    print(f"\n###################{title}####################" )
#1-D array
print_with_lines("1-D array")
arr=np.array([1, 2, 3, 4, 5])
print(arr)


#0-Dimensional
print_with_lines("0-D array")
arr=np.array(42)
print(arr)

#4-D array
print_with_lines("4-D array")
arr = np.array([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[31, 32, 33], [34, 35, 36], [37, 38, 39]]]])
print(arr)
print(arr[0][1])
print(arr[0][0][0][0])
print(arr.ndim)


#slicing
print_with_lines("slicing")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])