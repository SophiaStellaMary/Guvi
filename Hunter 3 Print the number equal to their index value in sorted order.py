''' Hunter 3 Print the number equal to their index value in sorted order '''
x = int(input())
y= list(map(int,input().split()))
z= []
for i in range(0,x):
  if(y[i]==i):
    z.append(i)
c=set(z)
if(len(c)==0):
  print('-1')
else:
  print(*c)
