'''Pro 52 check wheather the four points form a square or not'''
v,t=list(map(int,input().split()))
c,d=list(map(int,input().split()))
e,f=list(map(int,input().split()))
g,h=list(map(int,input().split()))
m=d-t
n=f-h
o=e-c
p=g-v
if (m==n==o==p):
    print("yes")
else:
    print("no")
