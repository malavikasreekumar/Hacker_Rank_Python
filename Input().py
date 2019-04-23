def val(x,k): 
    p=eval(input())

    o=int(p)
    if o==k:
        return(True) 
    else:
        return(False)

xint, kint = (input().split())
x=int(xint)
k=int(kint)
p=val(x,k)
print(p)
