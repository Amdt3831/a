columns = input()

map = [['.'] * int(columns)]
map[0][0] = '*'
o = ''
orders = []
while not o == 'END':
    order = input()
    orders.append(order)
    o = order

location = [0, 0]


def right():
    map[location[0]][location[1] + 1] = '*'
    location[1] += 1


def left():
    map[location[0]][location[1]-1] = '*'
    location[1] -= 1


def below():
    try:
        map[location[0]+1][location[1]] = '*'
        location[0] += 1
        return
    except IndexError:
        map.insert(location[0]+1, ['.'] * int(columns))
        map[location[0] + 1][location[1]] = '*'
        location[0] += 1


for item in orders:
    if item.startswith('R'):
        if not location[1]+1 == int(columns):
            right()
    elif item.startswith('L'):
        if not location[1]-1 == -1:
            left()
    elif item.startswith('B'):
        below()
    else:
        break

for i in range(len(map)):
    print(*map[i])

if not location[1] == int(columns)-1:
    print("There's no way out!")
elif location[0] != len(map)-1:
    print("There's no way out!")

