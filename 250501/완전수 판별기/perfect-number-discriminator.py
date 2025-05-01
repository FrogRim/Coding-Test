n = int(input())
sum_val = 0
result = []
for i in range(1,n):
    if n % i == 0:
        result.append(i)


for k in result:
    sum_val += k

if sum_val == n:
    print('P')
else:
    print('N')