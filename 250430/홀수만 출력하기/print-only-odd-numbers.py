n = int(input())

result = []

for i in range(1,n+1):
    num = int(input())
    if num % 3 == 0 and  num % 2 == 1:
        result.append(num)


for k in result:
    print(k) 