n = int(input())
arr = [input()
        for _ in range(n)]

word = input()

result = []
for temp in arr:
    if word == temp[0]:
        result.append(temp)




te = 0
for i in result:
    te += len(i)


print(f"{len(result)} {te/len(result):.2f}")