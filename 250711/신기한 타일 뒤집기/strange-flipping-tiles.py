n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)



# Please write your code here.
class Point:
    def __init__(self):
        self.state = None

    def paint_white(self):
        
        self._update_state("W")

    def paint_black(self):
        
        self._update_state("B")

    def _update_state(self, painted):
        self.state = painted

space = {}
current_pos = 0

for distance_str, direction in zip(x,dir):
    distance = int(distance_str)-1

    # 이동 방향과 범위 설정 (for문 안으로)
    if direction == 'L':
        start, end = current_pos - distance, current_pos 
  
        paint_method = 'white'
    else:  # direction == 'R'
        start, end = current_pos , current_pos + distance
        
        paint_method = 'black'

    # 색칠하기
    for pos in range(start, end+1):
        if pos not in space:
            space[pos] = Point()

        if paint_method == 'white':
            space[pos].paint_white()
        else:
            space[pos].paint_black()
        
    # 현재 위치 업데이트
    if direction == 'L':
        current_pos -= distance 
    else:
        current_pos += distance  

count_white = sum(1 for point in space.values() if point.state == 'W')
count_black = sum(1 for point in space.values() if point.state == 'B')

print(count_white, count_black)
