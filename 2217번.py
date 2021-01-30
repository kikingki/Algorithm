
import sys
input = sys.stdin.readline

# 들어올릴 수 있는 최대 중량을 반환하는 함수
def max_weight(n,rope):
    # 가장 무거운 무게를 들 수 있는 로프는 1개, 그 다음으로 무거운 무게를 들 수 있는 로프는 2개...
    # 따라서 최대 중량이 큰 순서(역순)로 정렬
    rope.sort(reverse=True)

    for i in range(n):
        rope[i] *= i+1  #i는 0부터 시작

    return max(rope)

n = int(input())
r = []

for _ in range(n):
    r.append(int(input()))

print(max_weight(n,r))
