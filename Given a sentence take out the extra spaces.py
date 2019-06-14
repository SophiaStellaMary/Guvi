'''PLAYER 26 given a sentence take out the extra spaces'''
M=list(map(str,input().split()))
for i in M:
    if i!=" ":
        print(i,end=' ')
