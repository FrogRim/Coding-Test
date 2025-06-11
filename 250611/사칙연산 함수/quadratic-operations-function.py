a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
o = str(o)

def switch(a,o,c):
  result = {"+" : a + c, "-": a - c, "/" : a // c, "*" : a * c}.get(o, "False")
  return result 

if switch(a, o, c) != 'False':
    print(f"{a} {o} {c} = {switch(a, o, c)}")
else:
    print(switch(a, o, c))
