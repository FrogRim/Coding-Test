a, b = map(int, input().split())
cnt = 0
# Please write your code here.
def sum1(n):
    h = n // 100
    t = n //10
    o = n % 10

    if (h+t+o) % 2 == 0:
        return True
    else:
        return False 

def is_prime(n):
    for j in range(2,n):
        if n % j == 0:
            return False
    return True


for i in range(a,b+1):
    if sum1(i) and is_prime(i):
        cnt+=1

print(cnt)