def GCD(a,b):
    while b:
        a,b = b,a%b
    return a
def LCM(a,b):
    return abs(a*b)//GCD(a,b)
n1=int(input())
n2=int(input())
ans=LCM(n1,n2)
print(ans)