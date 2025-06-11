Y, M, D = map(int, input().split())

def check_yun(n):
    if n % 4 == 0:
        if n % 100 != 0 or n % 400 == 0:
            return True  
   
    return False

def season(month):
  result = {1 : "Winter", 
            2 : "Winter",
            3 : "Spring", 
            4 : "Spring",
            5 : "Spring",
            6 : "Summer",
            7 : "Summer",
            8 : "Summer",
            9 : "Fall",
            10 : "Fall",
            11 : "Fall",
            12 : "Winter",
            }.get(month, None)
  return result 


# Please write your code here.
def check(y,a,b):
  if a == 2:
    if check_yun(y):
      if b < 30:
        return True
      else:
        if b < 29:
          return True
  else:
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
      return True
    else:
      if b != 31:
        return True
    
        

if check(Y,M,D):
  print(season(M))
else:
  print("-1")