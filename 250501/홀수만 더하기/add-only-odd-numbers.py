n = int(input())
sum_val = 0
for _ in range(n):
    i = int(input())
    if i % 3 == 0  and i % 2 == 1:
        sum_val += i

print(sum_val)
