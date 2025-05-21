n = 4
arr_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = 0

for i in range(n):
    for j in range(i+1):
        result += arr_2d[i][j]

print(result)