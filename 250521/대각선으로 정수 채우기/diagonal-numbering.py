n, m = map(int, input().split())


# 0으로 채워진 n x m 배열 생성
arr = [[0]*m for _ in range(n)]

val = 1
for diag in range(n + m - 1):  # 가능한 대각선 수
    for i in range(n):
        j = diag - i
        if 0 <= j < m:
            arr[i][j] = val
            val += 1

# 배열 출력
for row in arr:
    print(*row)
