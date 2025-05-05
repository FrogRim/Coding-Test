n = int(input())
cnt = 1
k = 1
for i in range(1,n+1):         
    while cnt <n+1:
        print("*"*k)
        k = 2*cnt+1
        cnt += 1
    print()
