
def func(n1 , op , n2):
    if op == "+":
        return (n1+n2)
    elif op == "-":
        return (n1-n2)
    elif op == "*":
        return (n1*n2)
    elif op == "/":
        if(n2 == 0):
            print("division not possible")
        else:    
            return (n1/n2)
    else:
        print("wrong operator") #if none of the operation match
        number1 = float(input("enter the first number = "))
        op = input("enter the operation (+ , - , * , /) = ")
        number2 = float(input("enter the second number = "))
        ans = func(number1 , op , number2)                
        return ans
        
number1 = float(input("enter the first number = "))
op = input("enter the operation (+ , - , * , /) = ")
number2 = float(input("enter the second number = "))  
ans = func(number1 , op , number2)
print(ans)      
