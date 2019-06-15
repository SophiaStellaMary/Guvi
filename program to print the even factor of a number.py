'''Player 38 program to print the even factor of a number'''
x=int(input())
for i in range(1, x + 1):
    if (x % i == 0):
        if (i % 2 == 0):
            print(i,end=" ")
        
