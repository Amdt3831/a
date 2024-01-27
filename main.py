import numpy as np
f = open('input1.txt', 'r')
inp = [line.strip().split(' ') for line in f.readlines()]
for i in range(1, len(inp)):
    for j in range(int(inp[0][1])):
        inp[i][j] = int(inp[i][j])
inp[0][0] = int(inp[0][0])
inp[0][1] = int(inp[0][1])
sets = {}
y = 1
for i in range(1, inp[0][0]+1):
    sets[f'sett{i}'] = list(np.array([]))
    u = 0
    while u < inp[0][1]:
        sets[f'sett{i}'].append(inp[y])
        y += 1
        u += 1
p = 0
item3 = 0
item4 = 0
for item1 in range(1, len(sets) + 1):
    for item2 in range(item1 + 1, len(sets) + 1):
        a = np.array(sets[f'sett{item1}'])
        b = np.array(sets[f'sett{item2}'])
        c = np.dot(a, b)
        if np.linalg.det(c) > p:
            p = np.linalg.det(c)
            item3 = item1
            item4 = item2

t = np.array(sets[f'sett{item3}'])
y = np.array(sets[f'sett{item4}'])
if np.linalg.det(t) > np.linalg.det(y):
    v = np.dot(t, y)
elif np.linalg.det(t) < np.linalg.det(y):
    v = np.dot(y, t)
else:
    v = np.dot(t, y)

g = np.around(np.linalg.inv(v), decimals=3)
for item in g:
    print(*item)

