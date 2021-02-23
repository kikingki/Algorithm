import sys
from collections import deque
input = sys.stdin.readline

# 익은 토마토의 주변이 익는 것이므로 BFS로 푸는 것이 적합
def bfs():
    # x값(좌,우)
    dx = [1, -1, 0, 0]
    # y값(아래,위)
    dy = [0, 0, -1, 1]

    # 토마토가 익는 날짜, 첫 반복부터 1을 더하므로 -1로 선언
    days = -1

    while queue:
        days += 1
        for _ in range(len(queue)):
            # 익은 토마토의 좌표
            a, b = queue.popleft()

            # 상하좌우 검사
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]

                # x,y가 n,m의 범위 안이면서 아직 안 익은 토마토일 경우
                if 0 <= x < n and 0 <= y < m and box[x][y] == 0:
                    box[x][y] = box[a][b] + 1
                    queue.append([x, y])

    for b in box:
        # BFS 후 박스 안에 안익은 토마토가 있는 경우
        if 0 in b:
            return -1
    return days

# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수
m, n = map(int, input().split())

# 상자에 담긴 토마토의 정보를 입력받음
box = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

# 익은 토마토 위치 파악 후 위치를 queue에 push
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

print(bfs())



