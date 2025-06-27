unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Bomb:
    def __init__(self,unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds



b = Bomb(unlock_code, wire_color, seconds)

print(f"code : {unlock_code}")
print(f"color : {wire_color}")
print(f"second : {seconds}")

