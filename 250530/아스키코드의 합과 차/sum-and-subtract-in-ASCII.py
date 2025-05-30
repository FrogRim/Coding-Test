a,b = input().split(" ")
_sum  = ord(a)+ord(b)

if ord(a) > ord(b):
    _dif = ord(a) - ord(b)
else:
    _dif = ord(b) - ord(a)

print(f"{_sum} {_dif}")

