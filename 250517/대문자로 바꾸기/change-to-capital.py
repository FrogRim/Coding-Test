n = 5
arr_2d = [
    list(input().split())
    for _ in range(n)
]

for i in range(5):
    for j in range(3):
        k = arr_2d[i][j].upper()
        print(k, end=" ")
    print()
