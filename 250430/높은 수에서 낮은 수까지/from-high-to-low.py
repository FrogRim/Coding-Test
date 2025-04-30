a,b = map(int,input().split())

larger = (a + b + abs(a - b)) // 2

if larger == a:
    for i in range(a,b-1,-1):
        print(i,end=' ')
else:
    for i in range(b,a-1,-1):
        print(i,end=' ')


