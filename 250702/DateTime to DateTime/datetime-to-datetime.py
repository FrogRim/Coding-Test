a, b, c = map(int, input().split())

# Please write your code here.
check = 0

d = 11
h = 11
m = 11

if (a == 11 and b < 11) or (a == 11 and b == 11 and c < 11):
    print(-1)

else:
    while True:
        if d == a and h == b and m == c:
            print(check)
            break

        m += 1
        check +=1

        if m == 60:
            h += 1
            m = 0

        if h == 24:
            d +=1
            h = 0 

