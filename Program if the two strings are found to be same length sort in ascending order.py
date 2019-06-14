'''Player 25 if the two strings are found to be same length sort in ascending order'''
l1=[]
m=int(input())
a=input().split()
for i in a:
  l1.append(i)
l1.sort()
l1.sort(key=len)
for i in l1:
  print (i,end=" ")
