def GCD(a,b):
    while b:
        a,b = b,a%b
    return a
n1=int(input())
n2=int(input())
ans=GCD(n1,n2)
print(ans)