n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Human:
    def __init__(self, name, street_address,region):
        self.name = name
        self.street_address = street_address
        self.region = region


humans = []
for i in range(n):
    tmp_name = name[i]
    tmp_adress = street_address[i]
    tmp_region = region[i]
    humans.append(Human(tmp_name,tmp_adress,tmp_region))


humans.sort(key= lambda x: x.name)

i = humans[-1]
print(f"name {i.name}")
print(f"addr {i.street_address}")
print(f"city {i.region}")
