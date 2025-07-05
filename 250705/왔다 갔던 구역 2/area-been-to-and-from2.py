n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

class Pos:
    def __init__(self,pos,num):
        self.pos = pos
        self.num = num

space = [Pos(i,0) for i in range(-1000,1001)]

cur_pos = 0

for order1,order2 in zip(x,dir):
    
    if order2 == 'R':
        for i in range(cur_pos,cur_pos+int(order1)+1):
            space[1000+i].num += 1
            cur_pos += order1
        
    elif order2 == 'L':
        for i in range(cur_pos,(cur_pos-int(order1)-1),-1):
            space[1000+i].num += 1
            cur_pos -= order1
        
result = 0
for t in space:
    if 1 < t.num:
        print(t.pos)
        result += 1

print(result)   