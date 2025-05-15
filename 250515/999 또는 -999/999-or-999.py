a = list(map(int,input().split()))
result1 = a[0]
result2 = a[0]

for i in a:
    if i == 999 or i == -999:
        break
    if i > result1:
        result1 = i
    if i < result2:
        result2 = i

print(f"{result1} {result2}")
