'''To find sum of arithematic progression '''
n,a,d=input().split()
n=int(n)
a=int(a)
d=int(d)
sum= (n*(2*a+(n-1)*d))/2
print(int(sum)) 
