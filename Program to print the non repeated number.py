''' Hunter 15 Print the non repeated number '''
N=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
  if(a.count(i)>1):
    b.append(i)
  else:
    print(i)
