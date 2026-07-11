base=int(input("enter the base: "))
power=int(input("enter the power: "))

result=1

for i in range(1,power+1):
    result=result*base
print(result)