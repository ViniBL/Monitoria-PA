s = input()
n = int(input())
c = input()

s = list(s)

if(n<len(s)):
    s[n] = c
else:
    s.append(c)
print("".join(s))