'''Hunter 47 remove extra spaces in string'''
M=list(map(str,input().split()))
for i in M:
    if i!=" ":
        print(i,end=' ')
    
