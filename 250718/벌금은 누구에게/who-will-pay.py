N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
result = [0 for _ in range(M)]


for s in student:
    result[s-1] += 1
    if result[s-1] == K:
        print(s)
        break
