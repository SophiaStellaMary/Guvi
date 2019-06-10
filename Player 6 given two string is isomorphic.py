'''Player 6 given two string is isomorphic'''
x,y=list(map(str,input().split()))
a=len(set(x))
b=len(set(y))
if a==b:
    print("yes")
else:
    print("no")
