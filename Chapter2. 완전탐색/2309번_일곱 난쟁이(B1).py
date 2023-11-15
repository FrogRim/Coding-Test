# 9개의 경우의 수에서 7개를 뽑는다 -> combination

from itertools import combinations


heights = [int(input()) for _ in range(9)] # 9번 숫자를 입력받아 height 리스트 안에 넣어 초기화.


# combinations은 모든 조합 경우의 수를 각각 튜플로 출력한다.

for i in combinations(heights,7): #combinations(어떤 배열, 몇개 뽑을건지)
    
	# 다 합쳐서 100이 되는 조합 찾기
    if sum(i) == 100:

        # 조건에 맞는 튜플을 오름차순 정렬 후 하나씩 출력
        for height in sorted(i):
            print(height)
        break # 답을 하나만 출력해야하기때문에 출력을 완료했으면 반복문을 탈출
		