m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
#num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

check = 0

m = m1
d = d1
ma = m2
da = d2

if m1 < m2:
    m = m1
    d = d1
    ma = m2
    da = d2

elif m1> m2:
    m = m2
    d = d2
    ma = m1
    da = d1

elif m1 == m2:
    if d1 < d2:
        m = m1
        d = d1
        ma = m2
        da = d2

    elif d1> d2:
        m = m2
        d = d2
        ma = m1
        da = d1

while True:
    if  m == ma and d == da:
        print(days[(check % 7)-1])

        break

    d += 1
    check +=1

