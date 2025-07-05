from collections import defaultdict

n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

visited = defaultdict(int)
cur_pos = 0

for steps, direction in zip(x, dir):
    if direction == 'R':
        for i in range(cur_pos, cur_pos + steps):
            visited[i] += 1
        cur_pos += steps
    elif direction == 'L':
        for i in range(cur_pos, cur_pos - steps, -1):
            visited[i] += 1
        cur_pos -= steps

# Count positions visited more than once
result = sum(1 for v in visited.values() if v > 1)
print(result)
