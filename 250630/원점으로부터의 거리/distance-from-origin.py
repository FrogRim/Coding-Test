n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

class Pt:
    def __init__(self, num, x1, y1):
        self.num = num
        self.x1 = x1
        self.y1 = y1
        self.sqrt1 = abs(x1) + abs(y1)

# 포인트 구조는 (i, (x, y)) 이므로 i는 무시하고, (x, y)만 꺼내야 함
pts = [Pt(i + 1, xy[0], xy[1]) for i, (_, xy) in enumerate(points)]

pts.sort(key=lambda t: t.sqrt1)

for pt in pts:
    print(f"{pt.num}")
