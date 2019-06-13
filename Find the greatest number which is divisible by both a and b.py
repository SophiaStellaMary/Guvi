'''Player 22 Find the greatest number which is divisible by both a and b'''
a,b=map(int,input().split())
L=[]
for i in range(1,b+1):
    if(a%i==0 and b%i==0):
        L.append(i)
print(max(L))
