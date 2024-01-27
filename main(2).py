import math as m
import sys

z = []
inp = input().split(' ')
while inp != ['-1', '-1']:
    n, b = int(inp[0]), int(inp[1])

    if not 2 <= b <= 9:
        print('invalid base!')
        sys.exit()

    z.append(n)
    z.append(b)
    inp = input().split(' ')

rs = []
for u in range(0, len(z), 2):
    r = 0
    for i in range(1, z[u]+1):
        if z[u] % i == 0:
            r += i
    rs.append(r)


def base(r, b):
    o = ''
    while r != 0:
        o += str(int(r % b))
        r = int(r / b)
    return o[::-1]


results = []
for t in range(0, len(rs)):
    results.append(base(rs[t], z[2*t+1]))

d = 0
for item in results:
    d += int(item)

print(d)
