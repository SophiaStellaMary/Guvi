'''Pro 17 Program to pair of numbers it adds to get given input'''
a,b=map(int,input().split())
m=list(map(int,input().split()))
count=0
for i in range(len(m)):
  for j in range(i+1,len(m)):
    if(m[i]+m[j]==q):
        count=count+1
        break
if(count==1):
   print("yes")
else:
   print("no") 
