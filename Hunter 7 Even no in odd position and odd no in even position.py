'''Hunter 7 Even no in odd position and odd no in even position'''
a=int(input())
b=list(map(int,input().split()))
for i in range(0,a):
    if(i%2==0):
        if(b[i]%2!=0):
            print(b[i],end=" ")
    elif(i%2!=0):
        if(b[i]%2==0):
            print(b[i],end=" ")
