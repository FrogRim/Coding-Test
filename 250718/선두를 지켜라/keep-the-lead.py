def process_commands(velocity, times):
    positions = [0]
    for vel, t in zip(velocity, times):
        for _ in range(t):
            positions.append(positions[-1] + vel)
    return positions

def check(a, b):
    if a > b:
        return "a"
    elif a < b:
        return "b"
    else:
        return "eq"

n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

positions_A = process_commands(v, t)[1:] 
positions_B = process_commands(v2, t2)[1:]

# 비교 리스트 만들기
status = []
for a, b in zip(positions_A, positions_B):
    status.append(check(a, b))

# 변화 횟수 세기
result = 0
prev_leader = None
just_equal = False

for i in range(len(status)):
    if status[i] == "eq":
        just_equal = True
        continue

    if just_equal:
        # eq 이후 처음으로 나타난 비슷지 않은 상태에서 비교
        if prev_leader is not None and status[i] != prev_leader:
            result += 1
        prev_leader = status[i]
        just_equal = False
    else:
        prev_leader = status[i]

print(result)

