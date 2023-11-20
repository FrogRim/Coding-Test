N,L = map(int,input().split())

coord = [False] * 1001 # 위치 전체를 나타내는 리스트(최대 1000개이기때문에 1001을 곱합)


for i in map(int,input().split()):
    coord[i] = True # 물이 새는 곳만 true로 변경

x = 0 # 현재좌표
ans = 0 #테이프 개수

while x < 1001:

    #구멍이 새는 곳이라면
    if coord[x]:
        ans += 1
        x += L

    else:
        x += 1

print(ans)

