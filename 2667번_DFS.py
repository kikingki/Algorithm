dx = [1, -1, 0, 0]      # x값(좌,우)
dy = [0, 0, -1, 1]      # y값(아래,위)
n = int(input())        # 지도의 크기
home = [list(map(int, input())) for _ in range(n)]      # N x N의 2차원 배열 지도

# 깊이 우선 탐색(DFS) - 재귀
def dfs(x, y):
    global cnt              # 전역변수 사용
    if x < 0 or x >= n or y < 0 or y >= n:          # 범위를 벗어날 경우
        return False

    if home[x][y] == 1:
        cnt += 1
        home[x][y] = 0         # 방문한 노드 다시 방문X

        for i in range(4):      # 4방향 검사
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)         # 재귀 호출
        return True
    return False

count = []    # 각 단지의 집의 수를 저장하는 배열
cnt = 0       # 각 단지의 집의 수
for i in range(n):
    for j in range(n):
        # 한 단지를 탐색한 후 cnt 초기화
        if dfs(i,j) == True:
            count.append(cnt)
            cnt = 0

count.sort()        # 오름차순
# 총 단지 수와 각 단지내 집의 수 출력
print(len(count))
[print(c) for c in count]