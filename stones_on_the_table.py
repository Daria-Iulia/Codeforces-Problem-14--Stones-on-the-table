i = int(input())
s= str(input())


def ch(s):
    contor=0
    for j in range(i-1):
        if s[j] == s[j + 1]:
            contor += 1
    return contor

result=ch(s)

print(result)