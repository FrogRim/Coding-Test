n,m = map(int,input().split())
lines = [input() for _ in range(2*n)]

arr_2d = [list(map(int, line.split())) for line in lines[:n]]
arr_2d1 = [list(map(int, line.split())) for line in lines[n:2*n+1]]  



for i in range(n):
    for j in range(m):
        if arr_2d[i][j] == arr_2d1[i][j]:
            print(0,end=" ")
        else:
            print(1,end=" ")

    print()

