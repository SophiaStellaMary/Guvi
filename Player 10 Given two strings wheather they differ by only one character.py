'''Player 10 Given two strings wheather they differ by only one character'''
a,b=input().split()
count=0
for i in range(len(a)):
    if a[i]!=b[i]:
        count+=1
if count==1:
    print("yes")
else:
    print("no")
