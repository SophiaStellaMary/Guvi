''' Player 31 PROGRAM TO CHECK THE GIVEN VALUE LIE IN SAME LINE '''
x,x1=map(int,input().split())
y,y1=map(int,input().split())
z,z1=map(int,input().split())
s= x*(y1-z1)+y*(z1-x1)+z*(x1-y1)
if(s==0):
  print("yes")
else:
  print("no")
