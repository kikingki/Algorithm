from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]      # x값(좌,우)
dy = [0, 0, -1, 1]      # y값(아래,위)

# 너비 우선 탐색 - 큐
def bfs():
    queue = deque()
    queue.append([0, 0])
    while queue:
        a, b = queue.popleft()
        # 현재 위치에서 상하좌우 검사
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            # x,y가 n,m의 범위 안이면서 이동가능할 경우 (0부터 시작하므로 x < n, y < m)
            if 0 <= x < n and 0 <= y < m and maze[x][y] == 1:
                maze[x][y] = maze[a][b] + 1
                queue.append([x, y])
    return maze[n-1][m-1]

n, m = map(int, input().split())        # N x M 크기의 배열
maze = [list(map(int, input().strip())) for _ in range(n)]     # 2차원 배열로 입력
print(bfs())