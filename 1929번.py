import math

# 에라토스테네스의 체 구현
def eratos(m):
    sieve = [True] * m
    sieve[0] = False
    sieve[1] = False
    # √N까지 확인하는 방법이 시간복잡도 O(√N)으로 가장 효율적
    s = int(math.sqrt(m))

    for i in range(2, s+1):
        # i가 소수이면 i의 배수들은 합성수이므로 False로 바꿈
        if sieve[i] == True:
            for j in range(i*i, m, i):
                sieve[j] = False
    return sieve

n, m = map(int, input().split())

# 소수 리스트
p_li = eratos(m+1)

#  M이상 N이하의 소수 출력
for i in range(n, len(p_li)):
    if p_li[i]:
        print(i)