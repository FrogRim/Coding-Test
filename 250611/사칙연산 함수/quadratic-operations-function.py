a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
o = str(o)

# python은 switch문이 없어 이렇게 dict와 get을 이용해 switch기능 구현
def switch(a,o,c):
  result = {"+" : a + c, "-": a - c, "/" : a // c, "*" : a * c}.get(o, "False")
  return result 

if switch(a, o, c) != 'False':
    print(f"{a} {o} {c} = {switch(a, o, c)}")
else:
    print(switch(a, o, c))
