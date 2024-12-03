def remove (l1) :
    l2=[]
    for element in l1:
        if element not in l2 :
            l2.append(element)
    return l2
    

l1=list(map(int,input().split()))
result = remove(l1)
print(result)