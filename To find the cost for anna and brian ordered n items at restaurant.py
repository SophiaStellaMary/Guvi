'''Pro 65 To find the cost for anna and brian ordered n items at restaurant '''
n,s = map(int,input().split())
c = list(map(int,input().split()))
amount = int(input())
total = (sum(c)-c[s])//2
if (amount==total):
  print("Bon Appetit")
else:
  print(amount-total)
