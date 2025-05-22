n = int(input())



arr = [[0]*n for _ in range(n)]
flag = True
val = 1
for dif in range(n-1,-1,-1):
    if flag == True:
        for i in range(n-1,-1,-1):
            arr[i][dif] = val
            val += 1
        flag = False
    else:
        for i in range(n):
            arr[i][dif] = val
            val += 1
        flag = True
    


for row in arr:
    print(*row)
