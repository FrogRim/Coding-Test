cnt = 0
n = int(input())
while n < 1000:
    if n % 2 == 0:
        n = 2 * n + 2
        if n >= 1000:
            break
    else:
        n = 3 * n + 1
        if n >= 1000:
            break
    cnt += 1
print(cnt)
