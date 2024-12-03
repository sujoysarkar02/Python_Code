def pali(s):
    s=s.replace(" ","").lower()
    return s==s[ : :-1]
a=input()
if pali(a):
    print("palindrome")
else :
    print("Not palindrome")