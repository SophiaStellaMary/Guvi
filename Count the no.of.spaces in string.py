''' Count the no.of.spaces in string  '''
character = input() 
count = 0
for i in range(len(character)):
  if(character[i]==" "):
    count=count+1
print(count)
