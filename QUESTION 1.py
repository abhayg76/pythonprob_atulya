def order(list , value):
    if ( value.lower() == "asc"):

        list.sort()
        return list
    elif value.lower() == "desc":
        list.sort(reverse = True)
        return list
    elif value.lower() == "none":    
        return list
    else:
        print("enter the value !")
        value2 = input("enter a value(asc , desc , none)")
        return order(list , value2)
        
        

list = eval(input("enter a list of numbers = "))
value = input("enter the function(asc , desc , none) = ")

newList = order(list , value)
print(newList)
