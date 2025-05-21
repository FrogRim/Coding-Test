
lines = [input() for _ in range(7)]

arr_2d = [list(map(int, line.split())) for line in lines[:3]]
arr_2d1 = [list(map(int, line.split())) for line in lines[4:7]]  


for i in range(3):
    for j in range(3):
        print(arr_2d[i][j] * arr_2d1[i][j] , end=" ")
    print()

