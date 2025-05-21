n,m = map(int,input().split())
arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]
num=0
for k in range(n):
    arr_2d[k][0] = k

for x in range(m):
    if x % 2 == 0:
        arr_2d[0][x] = num
        num += (2*n)
    else:
        arr_2d[0][x] = num - 1



for i in range(1,n):
    for j in range(1,m):
        if j % 2 == 0:
            arr_2d[i][j] = arr_2d[0][j] + arr_2d[i][0]
            
        else:
           arr_2d[i][j] = arr_2d[0][j] - arr_2d[i][0]
           


   
# 출력
for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()
