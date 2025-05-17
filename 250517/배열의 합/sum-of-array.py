n = 4
arr_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(n):
    k=0
    for j in range(n):
        k += (arr_2d[i][j])
    print(k)
