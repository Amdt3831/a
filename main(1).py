num1 = int(input())
num2 = int(input())
num3 = int(input())

num1 = '0' * (32-len(bin(num1))+2) + bin(num1)[2:]
num2 = '0' * (32-len(bin(num2))+2) + bin(num2)[2:]
numberOfInvites = [3] * num3
for x in range(num3):
    numberOfInvites[x] = int(input())

for x in range(num3):
    if (num2+num1)[63-numberOfInvites[x]] == '1':
        print('yes')
    else:
        print('no')