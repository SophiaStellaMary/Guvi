'''Program to print the number which is not repeated'''
a=int(input())
b=list(map(int,input().split()))
for i in b:
    if b.count(i)==1:
      print(i)
