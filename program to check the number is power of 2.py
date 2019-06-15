'''Player 39 program to check the number is power of 2'''
n=int(input())
for i in range(0,n+1):
    if i**2==n:
        print('yes')
        break
else:
    print('no')

        
