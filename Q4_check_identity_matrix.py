# Write a  program to take a 2-D array of order 3 X 3 and check
# whether that matrix is an identity matrix or not.
# Input:
# 1 0 0
# 0 1 0
# 0 0 1
import numpy
arr1=numpy.zeros((3,3),int)
for x in range(3):
    for y in range(3):
        num=int(input("Enter the elements of an array: "))
        arr1[x][y]=num      
if x==y and (arr1[x][y]==1):
    print("identity matrix")  
else:
    print("not identity matrix")
      
    

     

