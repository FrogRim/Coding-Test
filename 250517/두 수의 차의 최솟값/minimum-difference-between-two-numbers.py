n = int(input())
arr = list(map(int, input().split()))

num = 100
# Please write your code here.
for i in range(n):
    
    for j in range(i+1,n):
        tmp = arr[j]-arr[i]
        if tmp < num and tmp != 0:
            num = tmp


print(num)



