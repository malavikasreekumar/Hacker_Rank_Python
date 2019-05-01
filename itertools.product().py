
from itertools import product
a=[]
b=[]
a=map(int,input().split())
b=map(int,input().split())

c=[]
c=list(product(a,b))
for i in c:
    print(i, end=" ")
