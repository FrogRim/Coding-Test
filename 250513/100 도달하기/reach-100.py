b = int(input())
a = 1
arr = []
arr.append(a)
arr.append(b)

while True:
    c = a+b

    if c > 100:
        arr.append(c)
        break
    arr.append(c)
    if len(arr) % 2 != 0:
        a = c
    else:
        b = c

for i in arr:
    print(i,end=" ")