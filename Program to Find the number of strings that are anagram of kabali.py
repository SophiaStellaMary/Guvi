'''Player 18 Find the number of strings that are anagram of kabali'''
N=int(input())
count=0
l=[]
for i in range(N):
    l.append(input())
for i in range(N):
    if sorted(l[i])==sorted('kabali'):
        count=count+1
print(count)        
