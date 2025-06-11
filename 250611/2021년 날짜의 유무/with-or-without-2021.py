M, D = map(int, input().split())


# Please write your code here.
def check(a,b):
  if a < 13:
    if a == 2:
      if b < 29:
        return True
    elif a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
      if b < 32:
        return True
    else:
      if b < 31:
        return True
  return False
        

print("Yes" if check(M,D) == True else "No")