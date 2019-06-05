'''Print each element with it Index'''
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
  print(a[i],i)
