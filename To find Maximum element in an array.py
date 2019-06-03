''' Maximum element in an array '''
num=int(input())
array=input()
l=list(map(int,array.split(' ')))
max=l[0]
for i in range(1,num):
  if(l[i]>max):
    max=l[i]
print(max)
