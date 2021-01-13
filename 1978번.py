import sys
input = sys.stdin.readline

def prime_list(m):
    sieve = [True] * m      # 에라토스테네스의 체 리스트 생성
    sieve[0] = False
    sieve[1] = False

    s = int(math.sqrt(m))

    # √N까지 확인하는 방법이 시간복잡도 O(√N)으로 가장 효율적
    for i in range(2, s+1):
        # i가 소수이면 i의 배수들을 False로 바꿈
        if sieve[i] == True:
            for j in range(i*i, m, i):
                sieve[j] = False
    return sieve

n = int(input())
li = list(map(int, input().split()))    # 입력받는 리스트
li = li[:n]     # n까지 슬라이싱

# 받은 수 중 제일 큰 값으로 에라토스테네스의 체 사용
m = max(li)+1
p_li = prime_list(m)    # 소수 리스트
p_num = 0

# p_li 중 입력된 수의 개수만 p_num에 더함
for i in li:
    if p_li[i]:
        p_num += 1
print(p_num)
