
# 자연수의 범위 n, 수열의 원소 개수 m
n, m = map(int, input().split())
# 중복 체크 리스트
visited = [False] * n
# 수열 리스트
num_list = []

# return문
# 1. return result => result 반환
# 2. no return & no result => code_block 실행 후 종료 (None 반환)
# 3. return (no result) => 함수 즉시 종료

# Backtracking은 DFS로 구현
def dfs(depth):
    # 깊이가 m과 동일하면
    if depth == m:
        # 리스트를 문자열로 변환해 출력 후 함수 종료
        print(' '.join(map(str, num_list)))
        return

    for i in range(1, n):
        if visited[i]:      # visited가 true일 경우 중복
            continue

        visited[i] = True   # 탐색점을 true로 변경
        num_list.append(i+1)
        dfs(depth+1)        # recursion 사용
        visited[i] = False  # 탐색이 끝나면 다시 false로 변경
        num_list.pop()      # 출력 후 이전 연산 요소 제거

dfs(0)
