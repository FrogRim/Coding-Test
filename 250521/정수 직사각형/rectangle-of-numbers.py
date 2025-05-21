n, m = map(int,input().split())
arr_2d = [
    [(m*j)+i+1 for i in range(m)]
    for j in range(n)
]

for row in arr_2d:
    for cols in row:
        print(cols, end=" ")
    print()