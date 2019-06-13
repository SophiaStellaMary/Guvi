'''HUNTER 26 program to reverse the list and print the list'''
N=int(input())
K=list(map(int,input().split()))
t=[]
for i in K:
  t.append(i)
t.reverse()
print(*t,sep="->")
