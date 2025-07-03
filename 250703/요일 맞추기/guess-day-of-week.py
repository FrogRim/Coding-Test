m1, d1, m2, d2 = map(int, input().split())


month, day = m1, d1
elapsed_days = 0

# Please write your code here.
day_week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]


#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if month == m2 and day == d2:
        break

    if m2 < month or day > d2:
        elapsed_days -= 1
        day -= 1

        if day < 1:
            month -= 1
            day = num_of_days[month]
    
    else:
        elapsed_days += 1
        day += 1

        if day > num_of_days[month]:
            month += 1
            day = 1

print(day_week[elapsed_days % 7])
#print(elapsed_days % 7)
