import re
input = input()
a = input.split(' ')
b = []
c = []
for x in a:
    b.append(x[0])
    c.append(x[1:])

for u in range(len(c)):
    c[u] = int(c[u])
r = zip(b, c)
t = list(r)
t.sort(key= lambda x: x[1])
for u in range(len(t)):
    t[u] = list(t[u])
x = []
for g in t:
    x.append(g[0])
u = ''.join(x)
print(u)