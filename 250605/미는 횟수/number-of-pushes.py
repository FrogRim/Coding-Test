cnt = 0
a = input()
b = input()


for _ in range(len(a)-1):
    a = a[-1]+a[:-1]
    cnt += 1
    
    if b == a:
        print(cnt)
        break
    
    if cnt == len(a)-1:
        print(-1)

