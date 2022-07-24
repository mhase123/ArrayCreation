# WAP to take input from the user into an array and remove duplicate
# numbers.
# Input: [1 2 2 3 3 3 4 4 5]
# Output: 1 2 3 4 5
import array
size=int(input("Enter the size of an array: "))
arr1=array.array("i",[])
arr2=array.array("i",[])
# print(arr1)
for x in range(size):
    num=int(input("Enter the elements of an array: "))
    arr1.append(num)  
for x in range(len(arr1)):
    if arr1[x] not in arr2:
        arr2.append(arr1[x])
print(arr2)        
    
        



