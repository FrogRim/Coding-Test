from collections import defaultdict

n = int(input())
moves = [(int(x), d) for x, d in (input().split() for _ in range(n))]

visited_edges = defaultdict(int)
cur_pos = 0

for steps, direction in moves:
    if direction == 'R':
        for i in range(steps):
            # 간선 식별: (작은 위치, 큰 위치)
            edge = (cur_pos + i, cur_pos + i + 1)
            visited_edges[edge] += 1
        cur_pos += steps
    else:  # 'L'
        for i in range(steps):
            edge = (cur_pos - i - 1, cur_pos - i)
            visited_edges[edge] += 1
        cur_pos -= steps

# 두 번 이상 지난 간선 수
result = sum(1 for cnt in visited_edges.values() if cnt >= 2)
print(result)
