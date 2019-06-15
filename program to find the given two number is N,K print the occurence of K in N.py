'''Player 36 program to find the given two number is N,K print the occurence of K in N'''
N=input().split()
a=list(N[0])
sum=0
k=N[1]
for i in a:
    if k==i:
        sum=sum+1
print(sum)
