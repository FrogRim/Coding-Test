m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
day_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 날짜를 일 수로 변환하는 함수
def days_since_start(month, day):
    return sum(num_of_days[:month]) + day

# 경과 일 수 계산
start_days = days_since_start(m1, d1)
end_days = days_since_start(m2, d2)
elapsed_days = end_days - start_days

# 요일 출력
print(day_week[elapsed_days % 7])