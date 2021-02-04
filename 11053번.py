import sys
input = sys.stdin.readline

n = int(input())

# 입력받은 수열
arr = list(map(int, input().split()))
# arr[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이
dp = [1 for _ in range(n)]

# 원소를 하나 선택해(i) 이전 원소들(j)과 비교
for i in range(n):
    for j in range(i):
        # 현재 값이 이전 값보다 크고, 현재 원소의 이전 dp 최댓값을 구하고 그 길이에 1을 더한다.
        # 조건에서 dp[i] < dp[j]+1를 미리 판단하는 것이 속도가 더 빨랐다.
        if arr[i] > arr[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

print(max(dp))