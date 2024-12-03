def count(str):
    freq={}
    for char in str :
        if char !=' ':
            if char in freq :
                freq[char]+=1
            else :
                freq[char]=1
    return freq

a=input()
c= count(a)
print(c)