from collections import Counter

def solution(N, stages):
    fail_late = {}                  # 실패율
    player = len(stages)            # 스테이지에 도달한 플레이어 수
    fail_user = Counter(stages)     # 각 스테이지별 클리어 하지 못한 유저 수
    
    # 스테이지 N까지의 실패율 모두 계산
    for i in range(1, N+1):
        if player != 0 and fail_user.get(i):             # 0으로 나누기 오류 발생 방지 
            fail = fail_user.get(i)
            fail_late[i] = fail/player  # i번 스테이지의 실패율 계산
            player -= fail              # 다음 스테이지의 플레이어 수는 실패한 플레이어 수만큼 줄어듬  
        else:                           
            fail_late[i] = 0
    # 실패율(fail_late[x])을 기준으로 내림차순 정렬
    fail_late = sorted(fail_late, key=lambda x:fail_late[x], reverse=True)
    return fail_late