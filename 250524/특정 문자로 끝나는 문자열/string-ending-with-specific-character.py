arr = [input()
        for _ in range(10)]
n = input()
result = []
for temp in arr:
    if n == temp[-1]:
        result.append(temp)

for k in result:
    print(k)