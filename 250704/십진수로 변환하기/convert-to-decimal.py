binary = input()

# Please write your code here.\

binarys = []

for b in binary:
    binarys.append(int(b))


num = 0

for i in range(len(binarys)):
    num = num * 2 + binarys[i]

print(num)
