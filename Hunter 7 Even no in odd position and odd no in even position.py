'''Hunter 7 Even no in odd position and odd no in even position'''
x=int(input())
y=[int(x) for x in input().split()]
for i in range(0,x):
    if(i%2==0):
        if(y[i]%2!=0):
            print(y[i],end=" ")
    elif(i%2!=0):
        if(y[i]%2==0):
            print(y[i],end=" ")
