word = ['L', 'E', 'B', 'R', 'O', 'S']

# 해당 문자를 찾지 못했다면 -1
idx = -1

k = input()
# 문자 탐색
for i, char in enumerate(word):
    if char == k:
        idx = i

# 문자가 존재하지 않는 경우
if idx == -1:
    print("None")
else:
    print(idx)

