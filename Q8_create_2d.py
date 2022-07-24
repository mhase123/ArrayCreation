# Write a program to create a 2d array of integer elements.
# Take the number of rows and columns values from the user.
# And print a 2d array of numbers whose first digit is N,
# take the N value from the user.
# Input:
# Enter number of Rows = 2
# Enter number of Column = 2
# Enter value of N = 3
# Output:
# 3 30
# 31 32
import numpy
i=int(input("Enter number of Rows = "))
j=int(input("Enter number of columns = "))
n=int(input("Enter value of N = "))
arr1=numpy.zeros((i,j),int)
k=(n*9)+n
for x in range(i):
    for y in range(j):
        if x==0 and y==0:
            arr1[0][0]=n
        else:   
            arr1[x][y]=k
            k=k+1
print(arr1)        
