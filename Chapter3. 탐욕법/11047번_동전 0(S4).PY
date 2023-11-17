N,K = map(int,input().split())

coins = [int(input()) for _ in range(N)]

coins.reverse() # 단위를 높은 순부터 내림차순으로 변경
ans = 0

for coin in coins:
    ans += K // coin 
    K %= coin
    #print(f'coin: {coin}, K: {K}, ans: {ans}')

print(ans)















""" N,K = map(int,input().split())

money = [int(input()) for _ in range(N)]

newList = [x for x in money if x < K]
min_num = 0

i = len(newList) - 1

while(True):
   
    if(K == 0):
        break
    else:
        if(newList[i] > K):
            i -= 1
        else:
            K-= newList[i]
            min_num += 1


print(min_num) """