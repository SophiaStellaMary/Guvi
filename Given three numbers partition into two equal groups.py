'''Given three numbers partition into two equal groups'''
A,B,C = map(int,input().split())
if A%(B+C)==0:
    print("YES")
else:
    print("NO")
