# Input 10 numbers into a list
arr=[]
for i in range(10):
    num=int(input("enter a number:"))
    arr.append(num)
# Assume the first element is largest and smallest
largest=arr[0]
smallest=arr[0]
# Find largest and smallest elements
for num in arr:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
# Display the results
print("Array elements:",arr)
print("Largest number=",largest)
print("Smallest number=",smallest)