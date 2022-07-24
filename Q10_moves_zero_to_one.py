# WAP to convert all the zeros to ones and news to zeros in given array
# ip: [ [1,0,1]
# [0,1,1]
# [1,0,0] ]
# Op: [ [0,1,0]
# [1,0,0]
# [0,1,1]]
import numpy
arr1=numpy.zeros((3,3),int)
for x in range(3):
    for y in range(3):
        num=int(input("Enter the elements of an array: "))
        arr1[x][y]=num
print(arr1)
for x in range(3):
    for y in range(3):
        if arr1[x][y]==1:
            arr1[x][y]=0
        else:
            arr1[x][y]=1
print(arr1)            

