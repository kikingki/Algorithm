
n = int(input())
dp = [0 for _ in range(n+1)]

# 점화식: dp[N] = min(dp[N-1], dp[N//2] , dp[N//3]) + 1
for i in range(2, n+1):
    # 1을 뺄 경우 나오는 경우의 수 저장
    dp[i] = dp[i-1] + 1

    #2로 나누어질 경우 기존 1을 뺄 경우의 수와 비교하여 최솟값 저장
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1

    #3으로 나누어질 경우 기존 1을 뺄 경우의 수와 비교하여 최솟값 저장
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

print(dp[-1])
