num=int(input("enter the number: "))
reverse=0

while(num>0):
    last_digit=num%10                #to get the last digit of the number
    reverse=reverse*10+last_digit    #to store the reversed order of  the number
    num=num//10                      #to update the number(deleting the last digit) for further iteration.
    print(reverse)

print("reverse of number is: ",reverse)
