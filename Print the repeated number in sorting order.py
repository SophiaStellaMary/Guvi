''' Print the repeated number in sorting order '''
x=int(input())
y=list(map(int,input().split()))
z=[]
for i in y:
  if(y.count(i)>1):
    z.append(i)
c=set(z)
if(len(c)==0):
  print('unique')
else:
  print(*c)
