'''PLAYER 26 given a sentence take out the extra spaces'''
l=list(map(str,input().split()))
for i in l:
    if i!=" ":
        print(i,end=' ')
