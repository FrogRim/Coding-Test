n = int(input())
price = list(map(int, input().split()))

current = 0
# Please write your code here.
for i in range(n):
    
    for j in range(i+1,n):
        sell = price[j]-price[i]
        if sell > current:
            current = sell


print(current)



