from collections import deque

def solution(progresses, speeds):
    pg_deque=deque(progresses)
    sp_deque=deque(speeds)
    answer=[]

    while(pg_deque):
        # 한 번의 배포에 배포되는 기능의 수
        end = 0
        if(pg_deque[0]<100):
            # 하루의 개발 진도
            for i in range(len(pg_deque)):
                pg_deque.append(pg_deque.popleft()+sp_deque[i])
        else:
            while(pg_deque):
                # 진도가 100%가 넘은 기능을 모두 queue에서 제거
                if(pg_deque[0]>=100):
                    end += 1
                    pg_deque.popleft()
                    sp_deque.popleft()
                else:
                    break
            answer.append(end)
    return answer