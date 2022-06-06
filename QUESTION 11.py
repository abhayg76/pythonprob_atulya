num = int(input("enter the number = "))
store = num
num2 = 0 
i = 1
while(num!=0):
    i = num%10
    num2 = num2*10 + i
    num = num//10
   
if(num2 == store):
    print(store , "is a palindrome number ")
else:
    print(store ,  "is not a palindrome number")       
