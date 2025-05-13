a,b = map(int,input().split())


remainders = []
while a > 1:
    remainder = a % b
    remainders.append(remainder)
    a //= b

remainder_count = {x: remainders.count(x) for x in set(remainders)}

result = 0
for v in remainder_count.values():
    result += v ** 2

print(result)
