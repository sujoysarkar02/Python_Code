def myswap(a,b):
    a,b=b,a
    return a,b
x=int(input())
y=int(input())
print(f"before swap x ={x} & y ={y}")
p,q=myswap(x,y)
print(f"after swap x={p} & y= {q}")