num=int(input("enter the number: "))

even=0
odd=0

while(num>0):
    digit=num%10

    if(digit%2==0):
        even=even+1
    else:
        odd=odd+1

    num=num//10  

print("number of even digits is: ",even)
print("number of odd digits is: ",odd)