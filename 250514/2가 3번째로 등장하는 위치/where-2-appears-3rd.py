n = int(input())

word = [int(i) for i in input().split()]


# 해당 문자를 찾지 못했다면 -1
idx = -1
cnt = 1
k = 2
# 문자 탐색
for i, char in enumerate(word):
    if char == k:
        if cnt == 3:
            idx = i
            break
        else:
            cnt+=1

# 문자가 존재하지 않는 경우
if idx == -1:
    print("None")
else:
    print(idx+1)

