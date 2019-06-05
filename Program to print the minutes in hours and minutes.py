'''Program to print the minutes in hours and minutes'''
n=int(input())
if(n<60):
    print(0,n)
else:
    h=n//60
    m=n%60
    print(h,m)
