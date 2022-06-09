# dp[i] = dp[i-1]+dp[i-2]
def case(dp, n):
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    if n >= 4:
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

dp = [0 for _ in range(1001)]
ans = case(dp, int(input())) % 10007
print(ans)