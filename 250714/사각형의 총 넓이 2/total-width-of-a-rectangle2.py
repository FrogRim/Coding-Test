n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
offset = 100

board = [[ 0 for _ in range(offset * 2)] for _ in range(offset * 2)]


for i in range(n):
    x_min = min(x1[i] + offset, x2[i] + offset)
    y_min = min(y1[i] + offset, y2[i] + offset)

    x_max = max(x1[i] + offset, x2[i] + offset)  
    y_max = max(y1[i] + offset, y2[i] + offset) 

    for x in range(x_min,x_max):
        for y in range(y_min,y_max):
            board[x][y] += 1
           

print(sum(1 for b in board for c in b if c >= 1))
