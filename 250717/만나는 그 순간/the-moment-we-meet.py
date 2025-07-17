def process_commands(directions, times):
    positions = [0]
    for dir, t in zip(directions, times):
        step = 1 if dir == 'R' else -1
        for i in range(t):
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

result = -1

for i,val_a in enumerate(positions_A):
    for j,val_b in enumerate(positions_B):
        if i == j and val_a == val_b:
            result = val_a + 1
        

print(result)