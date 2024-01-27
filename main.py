initial_input = input().split()
a, b = int(e[0]), int(e[1])

def firstnum(a, b):
    numss = []
    if b >= a:
        for num in range(a, b + 1):
            r = 0
            for num1 in range(1, num + 1):
                if num % num1 == 0:
                    r += 1
            if r == 2:
                numss.append(1)
        print('main order - amount:', len(numss))
    else:
        for num in range(b, a + 1):
            r = 0
            for num1 in range(1, num + 1):
                if num % num1 == 0:
                    r += 1
            if r == 2:
                numss.append(1)
        print('reverse order - amount:', len(numss))

firstnum(a, b)
