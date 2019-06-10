'''Hunter 6 Program to print the first number which is repeated'''
a=int(input())
b=list(map(int,input().split()))
for i in b:
    if b.count(i)>1:
        print(i)
        break
else:
    print("unique")
