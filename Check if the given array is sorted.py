'''Player 42 check if the given array is sorted'''
a=int(input())
b=input().split()
v=[]
for i in sorted(b):
  v.append(i)
if(v==b):
  print("yes")
else:
  print("no")
