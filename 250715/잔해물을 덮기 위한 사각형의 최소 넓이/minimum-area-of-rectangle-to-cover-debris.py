x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
offset = 1000

board = [[ 0 for _ in range(offset * 2)] for _ in range(offset * 2)]


for x in range(x1[0] + offset,x2[0] + offset):
    for y in range(y1[0] + offset, y2[0] + offset):
        board[x][y] += 1
            
           
for x in range(x1[1] + offset, x2[1] + offset):
        for y in range(y1[1] + offset, y2[1] + offset):
            board[x][y] += 2

x_max = 0
x_min = 2001

y_max = 0
y_min = 2001

for x in range(x1[0] + offset,x2[0] + offset):
    for y in range(y1[0] + offset, y2[0] + offset):
        if board[x][y] == 1:
            if x > x_max:
                x_max = x
            if y > y_max:
                y_max = y
            if x < x_min:
                x_min = x
            if y < y_min:
                y_min = y

              
   


for xk in range(x_min,x_max+1):
    for yk in range(y_min,y_max+1):
        board[xk][yk] += 10
           

print(sum(1 for b in board for c in b if c >= 10))
