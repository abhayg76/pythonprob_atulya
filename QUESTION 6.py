start = int(input("enter the start of the range = "))
end = int(input("enter the end element of  the range= "))
print("the prime numbers are - ")
for i in range(start , end+1):
    if(i==1):
        continue
    cond = True
    for j in range(2 , i):
        if i%j == 0:
            cond = False
            break
    if (cond == True):
        print(i)    
