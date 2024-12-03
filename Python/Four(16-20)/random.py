import random

def randfloat(x,y):
    return random.randint(x,y)

a=int(input("low bound"))
b=int(input("upper bound"))

res=randfloat(a,b)
print(res)
