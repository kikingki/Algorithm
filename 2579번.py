import sys
input = sys.stdin.readline

# 계단의 개수
n = int(input())

# 각 계단의 점수
# stair = [int(input()) for _ in range(n)]
stair = [0 for _ in range(301)]

# 각 계단까지의 합의 최대 점수
# dp = [0 for _ in range(n)]
dp = [0 for _ in range(301)]

for i in range(n):
    stair[i] = int(input())

# 도착 계단을 무조건 밟아야 한다.
# 도착 계단의 전 계단을 밟지 않은 경우와 도착 계단의 전 계단을 밟은 경우의 두 가지 경우 중 최대 점수
# 점화식: dp[n] = max(dp[n-2]+stair[i], dp[n-3]+stair[i]+stair[i-1])
dp[0] = stair[0]
dp[1] = stair[0]+stair[1]
dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, n):
    dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i]

print(dp[n-1])