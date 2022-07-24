# WAP to move the all the 0's at end of the array
import numpy
arr1=numpy.array([1,2,3,0,0,5])
count=0
for x in range(len(arr1)):
    if arr1[x]!=0:
        arr1[count]=arr1[x]
        count+=1
while count<len(arr1):
    arr1[count]=0
    count+=1        
print(arr1)        
        

