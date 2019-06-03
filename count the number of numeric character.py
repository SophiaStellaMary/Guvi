'''count the number of numeric character'''
string =input()
count = 0
for a in string: 
    if (a.isnumeric()) == True: 
        count+= 1
    else: 
        continue
print(count) 
