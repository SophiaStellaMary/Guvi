'''Hunter 11 Program to reverse every word in the string'''
a=input().split()
for i in range(0,len(a)):
    print(a[i][::-1],end=" ")
