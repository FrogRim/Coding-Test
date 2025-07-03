m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
day_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 날짜를 일 수로 변환하는 함수
def days_since_start(month, day):
    return sum(num_of_days[:month]) + day

# 경과 일 수 계산
start_days = days_since_start(m1, d1)
end_days = days_since_start(m2, d2)
elapsed_days = end_days - start_days

result = day_week.index(A)
count = 0
# 요일 출력
# print((elapsed_days // int(result)))
# print((elapsed_days % int(result)))

for i in range(elapsed_days+1):
    if day_week[i % 7] == A:
        count +=1

print(count)