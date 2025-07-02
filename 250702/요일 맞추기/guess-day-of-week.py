m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
day_week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

k = 0

if m1 <= m2:
    w_l = num_of_days[m1:2]
    for i in w_l:
        k += i
    #print(k)

    check = k + (d2 - d1)

    print(day_week[check % 7]) 

else:
    w_l = num_of_days[m2:m1]
    for i in w_l:
        k += i
    #print(k)

    check = -(k + (d2 - d1))

    #print(check % 7)

    print(day_week[check % 7+2]) 


