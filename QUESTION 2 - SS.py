def credit(number):
    newString = ""
    for i in range(12):
        newString = newString + "*"
    for i in range(12 , 16):
        newString = newString + number[i]
    return newString    
number = input("enter the credit number = ")
if len(number) == 16:
    protected = credit(number)
    print(protected)
else:
    print("Wrong number")
    number = input("enter correct number = ")
    protected = credit(number)
    print(protected)    
