n, m = map(int, input().split())

# Please write your code here.


def print_rect(n,m):
    result = 0
    for i in range(1,10,1):
        if n % i == 0 and m % i == 0:
            result = i

    print(result)



print_rect(n,m)
