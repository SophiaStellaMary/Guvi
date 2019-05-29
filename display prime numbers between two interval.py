a,b=input().split()
a=int(a)
b=int(b)
l=[]
for c in range(a+1,b):
  if(c>1):
    for i in range(2,c):
        if(c%i==0):
          break
    else:
       l.append(c)
print(*l)
