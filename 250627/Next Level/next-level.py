user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Object:
    def __init__(self, ids="codetree", lv = 10):
        self.ids = ids
        self.lv = lv
        

Object1 = Object()
Object2 = Object(user2_id, user2_level)# 넘어간 값을 사용
print(f"user {Object1.ids} lv {Object1.lv}")
print(f"user {Object2.ids} lv {Object2.lv}")

