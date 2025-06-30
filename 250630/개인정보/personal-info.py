n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class Profile:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

profiles_name = []
profiles_height = []

for i in range(5):
    profiles_name.append(Profile(name[i],height[i],weight[i]))
    profiles_height.append(Profile(name[i],height[i],weight[i]))

profiles_name.sort(lambda x: x.name)
profiles_height.sort(lambda x: -x.height)

print("name")
for name_lists in profiles_name:
    print(f"{name_lists.name} {name_lists.height} {name_lists.weight}")

print()

print("height")
for height_lists in profiles_height:
    print(f"{height_lists.name} {height_lists.height} {height_lists.weight}")