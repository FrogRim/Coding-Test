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
class Profile:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

profiles_name = []


for i in range(n):
    profiles_name.append(Profile(name[i],height[i],weight[i]))
 

profiles_name.sort(lambda x: (x.height,-x.weight))


for name_lists in profiles_name:
    print(f"{name_lists.name} {name_lists.height} {name_lists.weight}")
