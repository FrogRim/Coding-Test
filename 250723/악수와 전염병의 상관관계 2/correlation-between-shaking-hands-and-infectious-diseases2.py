# N : 개발자의 수
# K : K번 이하로 악수하는동안 만 전염병 옮김 -> 최대값
# P : 처음 전염병에 걸린 개발자 -> INIT값
# T :  t(시간대), x,y(악수한 사람들)

N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.

class Developer:
    def __init__(self,num_handshake):
        self.num_handshake = num_handshake
        self.check = False # True면 감염


devleopers = [Developer(0) for _ in range(N)]

devleopers[P-1].check = True # 초기 감염자 설정

handshakes.sort(lambda x: x[0]) # 시간대 빠른 순으로 정렬

for (_,x,y) in handshakes:

   
    x_devloper = devleopers[x-1]
    y_devloper = devleopers[y-1]
    
    # 만약 둘 다 감염자가 아니라면
    if x_devloper.check == False and y_devloper.check == False:
        continue
    
    #둘다 감염자이면 전염 횟수만 증가
    elif x_devloper.check == True and y_devloper.check == True:
        x_devloper.num_handshake += 1
        y_devloper.num_handshake += 1
        # print(f" 3:{x_devloper.num_handshake}")
        # print(f" 3:{y_devloper.num_handshake}")

    
    # 둘 중 하나라도 감염자면
    elif x_devloper.check == True:
        if x_devloper.num_handshake < K:
            y_devloper.check = True
            x_devloper.num_handshake += 1
            # print(f"1:{x_devloper.num_handshake}")
            # print(f"1:{y_devloper.num_handshake}")
        

    
    elif y_devloper.check == True:
        if y_devloper.num_handshake < K:
            x_devloper.check = True
            y_devloper.num_handshake += 1
            # print(f" 2:{x_devloper.num_handshake}")
            # print(f" 2:{y_devloper.num_handshake}")


for i in devleopers:
    print(int(i.check), end="")