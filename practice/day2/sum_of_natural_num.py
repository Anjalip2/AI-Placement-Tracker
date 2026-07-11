sum=0
n=int(input("enter the number of natural numbers to sum: "))
for i in range(1,n+1):
    sum=sum+i
    print("sum is: ", sum)# when you want to print all iterations.
print("final sum is: ", sum)# when you just want to print the final sum.