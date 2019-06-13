'''Hunter 19 print the element that appeared in all array'''
X,Y=map(int,input().split())
L=[]
for i in range(X):
	s=set(map(int,input().split()))
	L.append(s)
c=s.intersection(*L)
print(*c)
