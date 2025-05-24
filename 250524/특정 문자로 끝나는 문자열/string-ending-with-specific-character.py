arr = [input()
        for _ in range(10)]
n = input()
result = []
for temp in arr:
    if n == temp[-1]:
        result.append(temp)

if len(result) == 0:
    print("None")
else:
    for k in result:
        print(k)