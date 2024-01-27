rows = int(input())
initial = [1, 1]

if rows>1:
    print(1)
    print(*initial)
    def rowWeWant(initial):
        lst = []
        for item in range(len(initial)-1):
            lst.append(initial[item]+initial[item+1])
        initial = [1]* (len(lst)+2)
        initial[0] = 1
        for i in range(len(lst)):
            initial[i+1] = lst[i]
        initial[len(lst)+1] = 1
        return initial

    for row in range(1, rows-1):
        initial = rowWeWant(initial)
        print(*initial)
else:
    print(1)