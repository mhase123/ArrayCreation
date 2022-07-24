import numpy
size=int(input("Enter the size of an array: "))
arr1=numpy.zeros(size,int)
for x in range(size):
    arr1[x]=int(input("Enter the array elements: "))
print(arr1)    