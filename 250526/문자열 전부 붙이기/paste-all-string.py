n = int(input())
arr = []
for _ in range(n):
    text = input()
    arr.append(text)
tot_str = "".join([x for x in arr])
print(tot_str)


