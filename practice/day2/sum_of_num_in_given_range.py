total=0 #sum is a built-in python function 
start=int(input("enter the start digit: "))
end=int(input("enter the end digit: "))
for i in range(start, end+1):
    total=total+i
    print(total)
print("final sum is: ",total)
