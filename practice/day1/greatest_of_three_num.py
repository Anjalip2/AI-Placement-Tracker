num1=int(input("enter the 1st number: "))
num2=int(input("enter the 2st number: "))
num3=int(input("enter the 3st number: "))

if(num1==num2==num3):
    print("all are equal!")
elif(num1>=num2 and num1>=num3):
    print("num1 is greatest")
elif(num2>=num1 and num2>=num3):
    print("num2 is greater")
else:
    print("num3 is greater")
