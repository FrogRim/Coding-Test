n, m = map(int, input().split())

# Please write your code here.


def print_rect(n,m):
    result1 = []
    result2 = []
    for i in range(1,10,1):
        if n % i == 0:
            result1.append(i)
            result1.append(n // i)
        if m % i == 0:
            result2.append(i)
            result2.append(m // i)
    
    total = [x for x in result1 if x in result1 and x in result2] 
    print(max(total))



print_rect(n,m)
