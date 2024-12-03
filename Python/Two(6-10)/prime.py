def prime(x):
    if x <= 1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False 
    return True

a=int(input())
b=prime(a)
if b == True :
    print("prime")
else :
    print("Not prime")