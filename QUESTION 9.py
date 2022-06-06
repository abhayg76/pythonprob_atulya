string = input("enter the string - ")
list = list(string)
list.sort()
newString = ''
for i in list:
    newString += i

print("sorted string is - " , newString )