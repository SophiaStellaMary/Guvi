'''HUNTER 14 Permutation of the string'''
from itertools import permutations
x=input()
y=permutations(x)
for i in list(y):
    print(''.join(i))
