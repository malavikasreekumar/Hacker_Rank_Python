word=input()

a=list(word)
#print(a)
a.sort()

b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]

for i in range(0,len(word)):
    if a[i].isnumeric():
        b.append(int(a[i]))
    elif a[i].isalpha():
        c.append(a[i])


for i in range(len(b)):
    if b[i]%2==0:
        d.append(b[i])
    else:
        e.append(b[i])
  

for i in range(len(c)):
    if c[i].islower():
        f.append(c[i])
    else:
        g.append(c[i])


h=f+g+e+d
for i in range(len(h)):
    print(h[i],end="")
