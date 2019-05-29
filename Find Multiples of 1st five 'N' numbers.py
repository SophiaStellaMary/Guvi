''' Multiples of 1st five 'N' numbers '''
num=int(input())
a=[]
for i in range(1,6):
  product=num*i 
  a.append(product)
print(*a)
  
