import string
def remove(s):
    trans = s.maketrans('','',string.punctuation)

    return s.translate(trans)


s=input()
clean = remove(s)
print(clean)