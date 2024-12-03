def large(a,b,c):
    if a>=b and a>=c :
        return a 
    elif b>=a and b>=c :
        return b
    else :
        return c
    
n1=float(input())
n2=float(input())
n3=float(input())
largest = large(n1,n2,n3)
print(largest)