a, b = map(int, input().split())

# Please write your code here.
def all_different(n):
    n = str(n)
    n = list(n)
    
    if '3' in n or '6' in n or '9' in n:
        return True

    return False


def is_magic_number(n):
    return n % 3 == 0 or all_different(n)


cnt = 0
for i in range(a, b+1):
    if is_magic_number(i):
    
        cnt += 1

print(cnt)

