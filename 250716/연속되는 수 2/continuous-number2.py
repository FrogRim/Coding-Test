n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt = 0
for i in range(n):
    if arr[i] != arr[i - 1] or i == 0:
        cnt += 1

print(cnt)
