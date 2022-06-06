def  double(string):
    newString = ''
    for i in string:
        newString += i*2
    return newString

string = input("enter the string = ")
new = double(string)
print("new string after doubling every element - " , new)
