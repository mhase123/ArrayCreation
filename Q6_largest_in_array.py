# WAP to find the third largest element from an array
# Ip: [ [1,2,4]
# [5,3,9]
# [8,6,11]]
# Op: third largest element is 8
import numpy 
arr1=numpy.zeros((3,3),int)
for x in range(3):
    for y in range(3):
        num=int(input("Enter the elements of an array: "))
        arr1[x][y]=num
print(arr1) 
arr2=arr1.flatten()
arr3=numpy.sort(arr2)
print(arr3[-3],"is the third last elements")

       