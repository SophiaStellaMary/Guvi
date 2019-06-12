'''Player 17 Print the smallest number which is divisible by both a and b'''
x,y=map(int,input().split())
z=100000
L=[]
for i in range(1,z+1):
    if i%x==0 and i%y==0:
        L.append(i)
print(min(L))
