'''Player 41 program for given number is power of another number'''
N,K=map(int,input().split())
while N>1:
    N=N/K
if N==1:
    print("yes")
else:
    print("no")
