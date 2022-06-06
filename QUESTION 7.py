array = eval(input("enter a list of numbers = "))
freqarr = {}
for i in array:
    if i not in freqarr:
        freqarr[i] = 0
    else:
        freqarr[i]+=1
maxelement = [list(freqarr.keys())[0]]
maxfreq = 0
for k in freqarr.keys():
    if freqarr[k] > maxfreq:
        maxelement.clear()
        maxelement.append(k)
        maxfreq = freqarr[k]
    elif freqarr[k] == maxfreq:
        maxelement.append(k)    

print("element with highest frequency = "  )
for i in maxelement :
    print(i)