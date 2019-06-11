''' Player 13 Print the sum of squares of the digits'''
a=list(map(int,input()))
sum=0
for i in range (0,len(a)):
    sum=sum+(a[i]**2)
print(sum)
