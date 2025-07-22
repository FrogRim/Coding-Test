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



# A, B의 시간 단위 위치 계산
positions = process_commands(d, t)[1:]  
positions_b = process_commands(d_b, t_b)[1:]


# 횟수 계산 (끝에 다다르면 움직이지 않음)
max_len = max(len(positions), len(positions_b))
positions += [positions[-1]] * (max_len - len(positions))
positions_b += [positions_b[-1]] * (max_len - len(positions_b))


result = 0
for i in range(1, max_len):
    if positions[i] == positions_b[i] and positions[i-1] != positions_b[i-1]:
        result += 1

print(result)