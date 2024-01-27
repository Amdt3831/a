num1 = int(input())
num2 = int(input())
num3 = int(input())

d = num1 ^ num2
c = num1 & num2
while c != 0:
    c = num1 & num2
    c = c << 1
    d = num1 ^ num2
    num1, num2 = c, d

print(d)
if d == num3:
    print('YES')
else:
    print('NO')
