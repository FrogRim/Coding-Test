n = 10
sum_val = 0
cnt = 0
for _ in range(n):
    i = int(input())
    if i >= 0 and i <=200:
        sum_val += i
        cnt +=1

print(f"{sum_val} {sum_val/cnt:.1f}")
