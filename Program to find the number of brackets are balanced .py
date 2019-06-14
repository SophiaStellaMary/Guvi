'''Player 31 Program to find the number of brackets are balanced '''
N=input()
N1=N.count("(")
N2=N.count(")")
if(N1==N2):
  print("yes")
else:
  print("no")
