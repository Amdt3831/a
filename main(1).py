a = input()

if a != 'lcd' and a != 'gcd' and a != 'max' and a != 'min' and a != 'average' and a != 'sum':
    print('Invalid command')
else:
    lst = []
    while a != 'end':
        lst.append(a)
        a = input()

    for i in range(1, len(lst)):
        lst[i] = int(lst[i])


    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a


    lcd = lambda a, b: a * b / gcd(a, b)


    def avr(lst):
        t = 0
        for item in lst:
            t += item
        a = t / len(lst)
        return round(a, 2)


    def sum(lst):
        t = 0
        for i in lst:
            t += i
        return t


    if lst[0] == 'lcd':
        while len(lst) > 2:
            a = lcd(lst[1], lst[2])
            lst.pop(1)
            lst[1] = a
        print(int(lst[1]))

    if lst[0] == 'sum':
        print(sum(lst[1:]))

    if lst[0] == 'gcd':
        while len(lst) > 2:
            a = gcd(lst[1], lst[2])
            lst.pop(1)
            lst[1] = a
        print(lst[1])

    if lst[0] == 'average':
        print(avr(lst[1:]))

    if lst[0] == 'max':
        print(max(lst[1:]))

    if lst[0] == 'min':
        print(min(lst[1:]))

