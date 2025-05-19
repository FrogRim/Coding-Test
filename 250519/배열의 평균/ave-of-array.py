
arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(2):
    k = 0
    for j in range(4):
        k += arr_2d[i][j]
    print(k/4,end=" ")

print()

for i in range(4):
    k = 0
    for j in range(2):
        k += arr_2d[j][i]
    print(k/2,end=" ")

print()
result = 0

for x in arr_2d:
    for k in x:
        result += k

print(result/8)