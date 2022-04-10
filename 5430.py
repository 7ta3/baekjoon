from collections import deque
T = int(input())
for _ in range(T):
    p = list(input()) # 수행할 함수
    n = int(input()) # 배열에 들어있는 수의 개수
    l = input() # 문자열로 받은 배열
    A = deque([]) # 실제 리스트로 배열 수정
    R = 1 # 방향 파라미터 -1인 경우 reverse 상황

    S = '' # 42와 같은 한 자리 이상 숫자 처리
    if len(l) != 2:
        for i in l:
            if i.isdigit():
                S += i
            elif i == ',' or i == ']':
                A.append(int(S))
                S = ''

    for i in p:
        if i == 'R': # 뒤집기
            if R == 1: R = -1
            else: R = 1
        elif i == 'D': # 버리기
            if not A: # 비어있는 배열에 함수가 불리면 error 처리
                print('error')
                break
            if R == 1: # 정방향인 경우
                A.popleft()
            else: # 역방향인 경우
                A.pop()
    else:
        if R == -1:
            A.reverse()
        ans = list(['['])
        for i in range(len(A)-1):
            ans.extend([str(A[i]), ','])
        if A:
            ans.append(str(A[-1]))
        ans.append(']')
        print(''.join(ans))

