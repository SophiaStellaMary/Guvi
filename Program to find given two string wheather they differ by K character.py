'''PLAYER 30 given two string wheather they differ by K character'''
a,b,d=input().split()
c=int(d)
y=0
l=0
for i in a:
  y+=1
for i in range(y):
  if a[i]!=b[i]:
    l+=1
if l==c:
  print("yes")
else:
  print("no")
