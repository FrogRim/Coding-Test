def process_commands(velocity, times):
    # 각 시간마다 위치를 계산하여 누적 위치 리스트를 반환
    positions = [0]  # 시작 위치는 0
    for vel, t in zip(velocity, times):
        for _ in range(t):  # 시간 단위로 반복
            positions.append(positions[-1] + vel)
    return positions

def check(a, b):
    # A와 B의 위치를 비교해서 누가 앞서는지 판단
    if a > b:
        return "a"
    elif a < b:
        return "b"
    else:
        return "eq"  # 위치가 같으면 동률

# 입력 받기
n, m = map(int, input().split())

# A의 속도와 시간 정보 입력 받기
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# B의 속도와 시간 정보 입력 받기
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# A, B의 시간 단위 위치 계산
positions_A = process_commands(v, t)[1:]  # 첫 위치 0 제외
positions_B = process_commands(v2, t2)[1:]

# A와 B 위치 비교하여 상태 리스트 생성
status = []
for a, b in zip(positions_A, positions_B):
    status.append(check(a, b))

# 선두 변경 횟수 계산
result = 0
prev_leader = None  # 이전 선두 ("a" 또는 "b")

for s in status:
    if s == "eq":
        continue  # 동률이면 패스
    if prev_leader is None:
        prev_leader = s  # 첫 선두 설정
    elif s != prev_leader:
        result += 1  # 선두가 바뀌었으면 카운트
        prev_leader = s  # 현재 선두를 저장

print(result)
