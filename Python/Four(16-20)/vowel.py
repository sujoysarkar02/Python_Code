def count(s):
    vowel = "aeiouAEIOU"
    c=0
    for char in s :
        if char in vowel :
            c+=1
    return c

a=input()
ans=count(a)
print(ans)