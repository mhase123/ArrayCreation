# Write a program to take a 2-D array of order 3 X 3 and swap 1st
# row with 3rd row and print it as before and after operation.
import numpy
arr1=numpy.zeros((3,3),int)
for x in range(3):
    for y in range(3):
        num=int(input("Enter the array elements: "))
        arr1[x][y]=num
print(arr1)
print()
arr1[[0, 2]] = arr1[[2, 0]]
print(arr1)