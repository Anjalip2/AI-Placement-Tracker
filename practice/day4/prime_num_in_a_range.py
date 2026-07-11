start=int(input("enter the starting point: "))
end=int(input("enter the ending point: "))

for i in range(start,end+1):
    count=0

    for j in range(1,i+1):
        if(i%j==0):
            count=count+1

    if(count==2):
        print("prime: ",i)