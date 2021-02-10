import sys
input = sys.stdin.readline

# 계단의 개수
n = int(input())
# 각 계단의 점수
st = [int(input()) for _ in range(n)]
# 각 계단까지의 합의 최대 점수
dp = []

# 도착 계단을 무조건 밟아야 한다.
# 도착 계단의 전 계단을 밟지 않은 경우와 전 계단을 밟은 경우의 두 가지 경우 중 최대 점수
# 점화식: dp[n] = max(dp[n-2]+st[i], dp[n-3]+st[i]+st[i-1])
dp.append(st[0])
dp.append(max(st[0]+st[1], st[1]))
dp.append(max(st[0]+st[2], st[1]+st[2]))

for i in range(3, n):
    dp.append(max(dp[i-2] + st[i], dp[i-3] + st[i] + st[i-1]))

print(dp[-1])