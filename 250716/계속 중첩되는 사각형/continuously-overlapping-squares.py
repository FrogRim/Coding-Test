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
board = [[ "None" for _ in range(offset * 2)] for _ in range(offset * 2)]


for i in range(n):
    
    for x in range(x1[i] + offset,x2[i]+ offset):
        for y in range(y1[i] + offset, y2[i] + offset):
            
            # red
            if i % 2 == 0:
                board[x][y] = 'red'
            else:
                board[x][y] = "blue"




print(sum(1 for b in board for c in b if c  == "blue"))
