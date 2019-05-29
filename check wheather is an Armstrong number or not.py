''' check wheather is an Armstrong number  '''
num=int(input())
temp=num
count=0
while(temp > 0):
   digit = temp % 10
   count += digit ** 3
   temp //= 10
if(num==count):
   print("yes")
else:
   print("no")
