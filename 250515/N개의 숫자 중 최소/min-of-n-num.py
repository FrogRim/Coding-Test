n = int(input())
a = list(map(int, input().split()))

min_val = a[0]
for elem in a[1:]:
     if min_val > elem:
        min_val = elem

print(f"{min_val} {a.count(min_val)}")


