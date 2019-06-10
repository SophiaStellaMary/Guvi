'''Hunter 8 b[i]+b[j]==b[k]'''
a=int(input())
b=list(map(int,input().split()))
l=[]
for i in range(0,len(b)-2):
  for j in range(i+1,len(b)-1):
    for k in range(j+1,len(b)):
      if b[i]+b[j]==b[k]:
        l.append([b[i],b[j],b[k]])
for i in l:
  print(*i)
