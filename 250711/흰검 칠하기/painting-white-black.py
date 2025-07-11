n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

class Point:
    def __init__(self):
        self.cnt_w = 0
        self.cnt_b = 0
        self.state = 'None'

    def paint_white(self):
        self.cnt_w += 1
        self._update_state("W")

    def paint_black(self):
        self.cnt_b += 1
        self._update_state("B")

    def _update_state(self, painted):
        if self.cnt_w > 1 and self.cnt_b > 1:
            self.state = "G"
            
        else:
            self.state = painted

space = {}
current_pos = 0

for distance_str, direction in commands:
    distance = int(distance_str) - 1

    # 이동 방향과 범위 설정 (for문 안으로)
    if direction == 'L':
        start, end = current_pos - distance, current_pos + 1
  
        paint_method = 'white'
    else:  # direction == 'R'
        start, end = current_pos , current_pos + distance + 1
        
        paint_method = 'black'

    # 색칠하기
    for pos in range(start, end):
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
count_gray = sum(1 for point in space.values() if point.state == 'G')

print(count_white, count_black, count_gray)
