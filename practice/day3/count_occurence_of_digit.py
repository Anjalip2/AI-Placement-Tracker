num=int(input("enter the number: "))
digit=int(input("enter the digit to count: "))

count=0

while(num>0):
    last_digit=num%10
    
    if(digit==last_digit):
        count=count+1
    
    num=num//10

print("number", digit, "occured", count, "times.")