n = int(input())

# Please write your code here.
def is_magic_number(n):
    return n % 2 == 0

def k(n):
    return ((n % 10)+(n//10)) % 5 == 0


if is_magic_number(n) and k(n):
    print("Yes")
else:
    print("No")



