import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())            # 층
    n = int(input())            # 호
    apartment = [[0]*(n+1) for _ in range(k+1)]

    # 0층부터 초기화
    for j in range(n+1):
        apartment[0][j] = j

    for i in range(1, k+1):
        for j in range(1, n+1):
            apartment[i][j] = apartment[i - 1][j] + apartment[i][j-1]
    print(apartment[i][j])