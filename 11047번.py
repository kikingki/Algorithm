# 동전의 가치 Ai가 오름차순 정렬이고, i ≥ 2인 경우에 Ai는 A(i-1)의 배수라는 조건때문에 그리디 알고리즘을 사용해 동전 개수의 최솟값을 구할 수 있다.

n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))  #오름차순

cnt = 0
# k가 0이 되면 반복문 종료
while k > 0:
    # 역순으로 반복
    for i in range(len(a)-1, -1, -1):
        if k // a[i]:
            cnt += k//a[i]  # a[i]로 나눠지는 동전의 개수
            k = k % a[i]    # a[i]로 나눈 나머지 k원
print(cnt)
