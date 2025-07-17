def process_commands(directions, times):
    positions = [0]
    for dir, t in zip(directions, times):
        step = 1 if dir == 'R' else -1
        for _ in range(t):
            positions.append(positions[-1] + step)
    return positions

n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

positions_A = process_commands(d, t)
positions_B = process_commands(d2, t2)

positions_A.pop(0)  # 0 위치 제거
positions_B.pop(0)

result = -1

for i, (val_a, val_b) in enumerate(zip(positions_A, positions_B)):
    if val_a == val_b:
        result = i + 1  
        break

print(result)
