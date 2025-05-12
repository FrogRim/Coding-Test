a,b = map(int,input().split())

arr = []
arr.append(a)
arr.append(b)

while len(arr) != 10:
    c = a+b
    arr.append(c % 10)
    if len(arr) % 2 != 0:
        a = c
    else:
        b = c

for i in arr:
    print(i,end=" ")