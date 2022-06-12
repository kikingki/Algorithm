from collections import deque

dx = [1, -1, 0, 0]  # x값(좌,우)
dy = [0, 0, -1, 1]  # y값(아래,위)

# 너비 우선 탐색 - 큐
def bfs(home, x, y):
    queue = deque()
    queue.append([x, y])        # 시작점 queue에 추가
    home[x][y] = 0              # 방문한 노드 다시 방문하지 않도록 0으로 수정
    cnt = 1                     # 해당 단지의 집의 개수
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 상하좌우 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >= n:   # 범위를 벗어날 경우
                continue
            if home[nx][ny] == 1:           # 연결된 집이 있는 경우
                home[nx][ny] = 0            # 방문한 노드 다시 방문하지 않도록 0으로 수정
                queue.append([nx, ny])      # 해당 노드 queue에 추가
                cnt += 1
    return cnt

n = int(input())

home = [list(map(int, input())) for _ in range(n)]          # N x N의 지도
count = [bfs(home, i, j) for i in range(n) for j in range(n) if home[i][j] == 1]    # 각 단지의 집의 수를 저장하는 배열
count.sort()        # 오름차순

# 총 단지 수와 각 단지내 집의 수 출력
print(len(count))
[print(c) for c in count]