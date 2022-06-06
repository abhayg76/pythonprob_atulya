string = input('enter a string = ')
sum = 0
for i in string:
    if i.isnumeric()== True:
        sum = sum + int(i)

print("the sum of the numbers = " , sum)        