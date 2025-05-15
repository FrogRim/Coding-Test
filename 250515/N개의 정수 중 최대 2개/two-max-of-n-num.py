n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
a1 = sorted(a,reverse=True)


print(f"{a1[0]} {a1[1]}")
