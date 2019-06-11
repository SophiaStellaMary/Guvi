'''Player 14 Print the reversed string after removing the vowels'''
a=int(input())
string=input()
b=string[::-1]
for i in b:
  if(i!='A' and i!='E' and i!='I' and i!='O' and i!='U' and i!='a' and i!='e' and i!='i' and i!='o' and i!='u'):
    print(i,end="")
