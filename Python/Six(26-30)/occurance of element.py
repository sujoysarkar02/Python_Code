l1=list(map(int,input().split()))
element_count ={}
for element in l1 :
    if element in element_count :
        element_count[element]+=1
    else :
        element_count[element]=1

for element,count in element_count.items():
    print(f"{element} {count}")