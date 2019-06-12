'''Player 15 Given a string print a most repeated letter'''
string=input()
j=string[0]
for i in string:
    if (string.count(j)<string.count(i)):
        j=i
print(j)
