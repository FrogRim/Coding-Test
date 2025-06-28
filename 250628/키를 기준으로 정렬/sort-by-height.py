n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

humans = []

for i in range(n):
    humans.append(Human(name[i],height[i],weight[i]))

humans.sort(key=lambda x: x.height) # 국어 점수 기준 내림차순 정렬

for human in humans: # 정렬 이후의 결과 출력
    print(human.name, human.height, human.weight)

