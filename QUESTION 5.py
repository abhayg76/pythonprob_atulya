list = eval(input("enter a list of numbers = "))
list.sort()
for i in range(99):
    if list[i] == list[i+1]:
        print("the duplicate number is = " , list[i])
        break
