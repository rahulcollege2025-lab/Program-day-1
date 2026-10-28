# Input 5 numbers into a list
arr=[]
for i in range(5):
    num=int(input("Enter a number"))
    arr.append(num)
# Display the original array
print("Original array:",arr)
# Display the array in reverse order
print("Reversed array:",end=" ")
for i in range(4,-1,-1):
    print(arr[i],end=" ")
print()