num1 = int(input())
num2 = int(input())

num3 = num1 ^ num2
output = 0
for i in range(len(bin(num3))):
    if bin(num3)[i] == '1':
        output += 1
print(output)
