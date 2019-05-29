#Find out the even numbers between two interval
a,b=input().split()
a=int(a)
b=int(b)
l=[]
for i in range(a+1,b):
  if(i%2==0):
    l.append(i)
print(*l)
