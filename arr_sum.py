# Input 5 numbers into a list
arr=[]
for i in range(5):
    num=int(input("Enter a number:"))
    arr.append(num)
# Calculate sum and average
total=sum(arr)
average=total/5
# Display the results
print("Array elements:",arr)
print("sum=",total)
print("average=",average)