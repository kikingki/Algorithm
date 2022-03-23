from collections import deque

def solution(priorities, location):
    # enumerate() 함수를 사용해 튜플을 deque의 원소로 넣음.
    # max 함수에서 key가 아니라 value 값을 비교해야 하므로 v,i의 순으로 저장
    deq = deque([(v, i) for i, v in enumerate(priorities)])
    # 인쇄 요청한 문서의 인쇄 순서
    cnt = 0
    while deq:
        temp = deq.popleft()
        # popleft() 후 deque가 비어있는지 확인 and deq의 최댓값 value와 첫번째 문서의 value 비교
        if deq and temp[0] < max(deq)[0]:
            deq.append(temp)
        # 첫번째 문서가 가장 중요도가 높아야 인쇄됨.
        else:
            cnt += 1
            # 인쇄되는 문서의 index 값과 location이 동일하면 요청한 인쇄가 인쇄되는 것이므로 for문 종료
            if temp[1] == location:
                break
    return cnt