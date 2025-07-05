n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

class Point:
    def __init__(self,positon,num):
        self.positon = positon
        self.num = num


    
space = [Point(i,0) for i in range(-100,101)]

for s in segments:
    for k in range(s[0],s[1]):

        space[100 + k].num += 1

result = 0
for t in space:
    if result < t.num:
        result = t.num




print(result)

