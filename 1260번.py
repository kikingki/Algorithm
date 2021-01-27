import sys
from collections import deque
input = sys.stdin.readline

# 깊이 우선 탐색 - 스택
def dfs(graph, start):
    visited = []
    stack = deque([start])

    while stack:
        # 후입선출(LIFO)
        current = stack.pop()
        # 정점에 방문하지 않았을 경우
        if current not in visited:
            visited.append(current)
            # KeyError 방지
            if current in graph:
                # 방문할 수 있는 정점이 여러개인 경우, 정점 번호가 작은 것을 방문 - stack이므로 내림차순 정렬
                stack.extend(sorted(graph[current], reverse=True))

    return ' '.join(map(str,visited))   #문자열로 반환

# 너비 우선 탐색 - 큐
def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        # 선입선출(FIFO)
        current = queue.popleft()
        # 정점에 방문하지 않았을 경우
        if current not in visited:
            visited.append(current)
            # KeyError 방지
            if current in graph:
                # 방문할 수 있는 정점이 여러개인 경우, 정점 번호가 작은 것을 방문 - queue이므로 오름차순 정렬
                queue.extend(sorted(graph[current]))

    return ' '.join(map(str, visited))  #문자열로 반환

# 정점의 개수 n, 간선의 개수 m, 탐색을 시작할 정점의 번호 v
n, m, v = map(int, input().split())

# 딕셔너리
g = {}
for _ in range(m):
    x, y = map(int, input().split())
    # 양방향 연결이므로 x,y와 y,x 모두 연결
    # key의 value가 이미 있을 경우 append()로 value 추가
    # 아닐 경우 딕셔너리 쌍 추가
    if x in g:
        g[x].append(y)
    else:
        g[x] = [y]
    if y in g:
        g[y].append(x)
    else:
        g[y] = [x]

print(dfs(g, v))
print(bfs(g, v))
