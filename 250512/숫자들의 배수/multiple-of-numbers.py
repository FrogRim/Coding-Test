a = int(input())

arr = []
cnt = 0
i = 1
while cnt != 2:
    
    arr.append(a * i)
    if (a * i) % 5 == 0:
        cnt += 1
    i += 1

for i in arr:
    print(i,end=" ")