# dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
def case(n):
    if n <= 2:
        return n
    elif n == 3:
        return 4
    else:
        return case(n-1)+case(n-2)+case(n-3)

t = int(input())
for _ in range(t):
    c = case(int(input()))
    print(c)
