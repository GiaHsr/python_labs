a = input().split()
n = int(a[-1])
o = 0
z = 0
for i in range(n):
    s = input().split()
    if s[-1] == 'True': o += 1
    else: z += 1

print('out:', o, z)
