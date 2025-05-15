n = int(input())
a = list(map(int, input().split()))

max_val = -1

for elem in a:
    if a.count(elem) == 1:
        if elem > max_val:
            max_val = elem

print(max_val)

