a,b = map(int,input().split())
sum_val = 0

if a > b:
    large = a
    small = b

else:
    small = a
    large = b
for i in range(small, large + 1):
    if i % 5 == 0:
        sum_val += i
        

print(f"{sum_val}")
