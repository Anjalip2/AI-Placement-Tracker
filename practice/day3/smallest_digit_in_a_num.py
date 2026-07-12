num=int(input("enter the number: "))

smallest=num%10

while(num>0):
    digit=num%10

    if(digit<smallest):
        smallest=digit

    num=num//10

print("largest number is: ",smallest)