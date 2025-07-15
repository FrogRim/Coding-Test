n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

offset = 100
board = [[ 0 for _ in range(offset * 2)] for _ in range(offset * 2)]


for i in range(n):
    
    for x1 in range(x[i] + offset,x[i] + 8 + offset):
        for y1 in range(y[i] + offset, y[i] + 8 + offset):
            board[x1][y1] += 1



print(sum(1 for b in board for c in b if c > 0))

