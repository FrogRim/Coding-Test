x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.


offset = 1000

board = [[ 0 for _ in range(offset * 2)] for _ in range(offset * 2)]


for i in range(2):
    
    for x in range(x1[i] + offset,x2[i] + offset):
        for y in range(y1[i] + offset, y2[i] + offset):
            board[x][y] += 1
            
           
for x in range(x1[2] + offset, x2[2] + offset):
        for y in range(y1[2] + offset, y2[2] + offset):
            board[x][y] += 2


print(sum(1 for b in board for c in b if c == 1))

