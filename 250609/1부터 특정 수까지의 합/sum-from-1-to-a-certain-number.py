n = int(input())

# Please write your code here.
def add(n):
    total = 0
    for i in range(1,n+1):
        total += i

    return total // 10



total_num = add(n)

print(total_num)

