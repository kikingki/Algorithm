
n, m = map(int, input().split())
card = list(map(int, input().split()))  # 카드 리스트

temp = 0
approx = 0  # M에 가장 가까운 카드의 합

# 카드 3장의 합을 모두 구한다.
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            temp = card[i] + card[j] + card[k]
            if temp <= m:
                approx = max(approx, temp)  # 입력받은 매개변수들 중 가장 큰 값을 반환
print(approx)


