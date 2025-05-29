A = input()  # 문자열 A 입력
B = input()  # 문자열 B 입력

# 빈 문자열 B 처리
if not B:
    print(A)  # B가 빈 문자열이면 A를 그대로 출력
else:
    arr_A = list(A)  # A를 리스트로 변환하여 pop() 사용 가능하게 함
    len_b = len(B)  # B의 길이 저장
    while B in ''.join(arr_A):  # arr_A를 문자열로 변환해 B가 존재하는지 확인
        idx = (''.join(arr_A)).index(B)  # B의 첫 번째 발생 위치 찾기
        # idx에서 len_b만큼 문자 제거
        for _ in range(len_b):
            if idx < len(arr_A):  # 인덱스가 유효한지 확인
                arr_A.pop(idx)  # idx 위치에서 문자 제거
    # 최종 결과를 문자열로 변환하여 출력
    A = ''.join(arr_A)
    print(A)