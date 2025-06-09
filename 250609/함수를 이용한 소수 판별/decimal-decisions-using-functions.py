a, b = map(int, input().split())

# Please write your code here.
def is_prime(a,b):
    lst = []
    for i in range(a, b+1):
        check = False
        for j in range(2,i):
            if i % j == 0:
                check = True
        if check == False:
            lst.append(i)
    return lst

cnt = 0

lst = is_prime(a,b)

for x in lst:
   
    cnt += x

print(cnt)
