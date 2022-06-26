import heapq

def solution(scoville, K):
    if set(scoville) == {0}:      # 0으로만 구성될 경우 영원히 K를 넘지 못함  
        return -1
    answer = 0
    heapq.heapify(scoville)     # heapq 사용 (최소 힙)

    while scoville[0] < K:
        if len(scoville) >= 2:         
            new_s = heapq.heappop(scoville) + heapq.heappop(scoville)*2
            heapq.heappush(scoville, new_s)     # heapq에 삽입
            answer += 1                     
        else:           # heapq의 요소가 1개인데 K보다 작을 경우 실패
            if heapq.heappop(scoville) < K:
                return -1
    return answer

'''
# PriorityQueue 모듈을 이용한 풀이 - 시간 초과로 실패
from queue import PriorityQueue

def solution(scoville, K):
    if set(scoville) == {0}:
        return -1
    answer = 0
    queue = PriorityQueue()

    for s in scoville:  # 우선순위큐에 넣음
        queue.put(s)

    while len(scoville):
        global last
        a = queue.get()
        if a >= K:  # 첫번째 원소가 K보다 크면 모든 음식이 K 이상이 된 것
            last = a
            break
        b = queue.get()
        new_s = a + b * 2
        answer += 1
        queue.put(new_s)

    if last < K:
        return -1
    return answer
'''