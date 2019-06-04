'''Given a number N and array of integer N print the median element'''
n=int(input())
n1=list(map(int,input().split()))
n=len(n1)//2
n1.sort()
print(n1[n])
