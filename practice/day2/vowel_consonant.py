ch=input("enter the character: ")
if('A'<= ch <='Z') or ('a'<= ch <='z'):
    ch=ch.lower() #converts the character to lowercase.
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'): 
    #can also use 'if ch in "aeiou":' this also works
        print(ch +" is a vowel. ") #both are correct( + or ,)as it is string concatenation.
    else:
        print(ch," is a consonant.")
else:
    print("invalid input.")