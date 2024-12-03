def tri(a,b,c):
    if a**2 == b**2 + c**2 :
        return 0.5*b*c
    else :
        s=(a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**0.5
    
a=int(input())
b=int(input())
c=int(input())
t=tri(a,b,c)
print(t)