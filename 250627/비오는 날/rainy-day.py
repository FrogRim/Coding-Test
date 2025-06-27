n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather


weathers = []
for i in range(n):
    tmp_date = date[i]
    tmp_day = day[i]
    tmp_weather = weather[i]
    weathers.append(Weather(tmp_date,tmp_day,tmp_weather))

result = []

for w in weathers:
    if(w.weather == "Rain"):
        result.append(w)


result.sort(key= lambda x: x.date)

i = result[0]
print(f"{i.date} {i.day} {i.weather}")

