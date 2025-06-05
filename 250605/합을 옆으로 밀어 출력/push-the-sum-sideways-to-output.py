n = int(input())

total = 0
for _ in range(n):
    num = int(input())
    total += num

total = str(total)

total1 = total[1:]+total[0]

print(total1)