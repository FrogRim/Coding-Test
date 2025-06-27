product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Object:
    def __init__(self, ids="codetree", lv = 50):
        self.ids = ids
        self.lv = lv
        

Object1 = Object()
Object2 = Object(product_name, product_code)# 넘어간 값을 사용
print(f"product {Object1.lv} is {Object1.ids}")
print(f"product {Object2.lv} is {Object2.ids}")

