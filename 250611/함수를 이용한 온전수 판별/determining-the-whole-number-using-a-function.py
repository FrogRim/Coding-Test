a, b = map(int, input().split())
cnt = 0
# Please write your code here.
def onjeensu(n):
    if n % 2 != 0:
        if n % 10 != 5:
            if n % 3 != 0 or n % 9 == 0:
                return True
    
    return False

for i in range(a,b+1):
    if onjeensu(i):
        cnt+=1

print(cnt)