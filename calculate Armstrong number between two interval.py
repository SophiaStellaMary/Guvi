'''Armstrong number between two interval'''
x,y=input().split()
x=int(x)
y=int(y)
l=[]
for num in range(x+1, y):
   # initialize sum
   sum = 0
 
   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
      l.append(sum)
print(*l)
