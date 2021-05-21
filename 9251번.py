import sys
input = sys.stdin.readline

# 공백 제거
str1 = input().rstrip()
str2 = input().rstrip()

m = len(str1)
n = len(str2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        # 끝 문자열이 동일할 경우
        if (str1[i-1]==str2[j-1]): #인덱스이므로 -1
            dp[i][j] = dp[i-1][j-1]+1
        
        # 끝 문자열이 다를 경우
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]) #왼쪽과 위쪽 중 큰 값

print(dp[-1][-1])
