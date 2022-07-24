# Write a java program to take a 2-D array of order 3 X 3 and Sort
# that array in ascending order and print it as before and after operation.

import numpy
arr1=numpy.zeros((3,3,),int)
for x in range(3):
    for y in range(3):
        num=int(input("Enter the array elements: "))
        arr1[x][y]=num
print("Original array")        
print(arr1)
arr2=arr1.flatten()
arr3=numpy.sort(arr2)
print(arr3.reshape(3,3))
