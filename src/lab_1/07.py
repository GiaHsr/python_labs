s = input('in: ')
n = 0
r = 0
print('out: ', end = '')

for i in s:
    if i.isupper():
        print(i, end = '')
        break
    n += 1


for i in range(n + 1, len(s)):
    if s[i - 1] in '0123456789':
        print(s[i], end = '')
        r = i - n
        break

for i in range(n + 2*r, len(s), r):
    print(s[i], end = '')
print()