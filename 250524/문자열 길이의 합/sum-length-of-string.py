n = int(input())
arr = [
    input()
    for _ in range(n)
]

cnt = 0
total = 0
for term in arr:
    total += len(term)
    if term[0] == 'a':
        
        cnt += 1

print(f"{total} {cnt}")
