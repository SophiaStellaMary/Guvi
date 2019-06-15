'''Hunter 40 sum of the digit is a palindrome'''
N=int(input())
sum=0
for i in str(N):
    sum=sum+int(i)
a=str(sum)
if str(sum)==a[::-1]:
    print("YES")
else:
    print("NO")
    
