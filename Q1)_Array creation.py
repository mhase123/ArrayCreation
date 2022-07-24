import array
arr1=array.array('i',[])
size=int(input("Enter the size of an array: "))
for x in range(size):
    arr1.append(int(input("Enter the elements of array: ")))
print(arr1)   
