# 자연수의 범위 n, 수열의 원소 개수 m
n, m = map(int, input().split())
# 중복 체크 리스트
visited = [False] * n
# 수열 리스트
num_list = []

# Backtracking은 DFS로 구현
def dfs(depth):
    # 깊이가 m과 동일하면
    if depth == m:
        # 리스트를 문자열로 변환해 출력 후 함수 종료
        print(*num_list)
        return

    for i in range(n):
        if visited[i]:  # visited가 true일 경우 중복
            continue

        visited[i] = True  # 탐색점을 true로 변경
        num_list.append(i + 1)
        dfs(depth + 1)  # recursion 사용
        num_list.pop()  # 출력 후 요소 제거

        # 고른 수열이 오름차순이어야 한다는 조건 => 즉, 순열이 아닌 조합
        # 탐색시작점 visited[i]를 제외하고 그 이후부터 False로 변경한다.
        for j in range(i + 1, n):
            visited[j] = False

dfs(0)