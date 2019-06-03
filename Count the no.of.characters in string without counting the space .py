''' Count the no.of.characters in string without counting the space '''
character = input() 
count = 0
for i in range(len(character)):
  if(character[i]==" "):
    continue
  count=count+1
print(count)
