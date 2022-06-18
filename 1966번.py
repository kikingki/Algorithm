from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())    # 문서의 개수, 궁금한 문서의 Queue의 위치
    document = list(map(int, input().split()))
    queue = deque((v, idx) for idx, v in enumerate(document))
    cnt = 0

    while queue:
        temp = queue.popleft()
        if queue and temp[0] < max(queue)[0]:
            queue.append(temp)
        else:
            cnt += 1
            if temp[1] == m:
                break
    print(cnt)




