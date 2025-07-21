n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
def process_commands(directions, times):
    positions = [0]
    for dir, t in zip(directions, times):
        step = 1 if dir == 'R' else -1
        for _ in range(t):
            positions.append(positions[-1] + step)
    return positions

positions = process_commands(d, t)
positions_b = process_commands(d_b, t_b)

positions.pop(0)  # 0 위치 제거
positions_b.pop(0)

result = -1

for i, (val_a, val_b) in enumerate(zip(positions, positions_b)):
    if val_a == val_b:
        result += 1  
        

print(result)
