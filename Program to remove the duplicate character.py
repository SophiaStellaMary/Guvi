'''Hunter 28 Program to remove the duplicate character'''
x=input()
L=""
for i in x:
 if i not in L:
     L=L+i
print(L)
