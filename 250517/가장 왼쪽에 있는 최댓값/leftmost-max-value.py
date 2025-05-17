n = int(input())
a = list(map(int, input().split()))

while a:
    max_val = max(a)

    
    for i in range(len(a)):
        if a[i] == max_val:
            print(i + 1, end=' ')
            a = a[:i]
            break
