import sys
input = sys.stdin.readline

n = int(input())
coordinate = []

# 각 점의 좌표 2차원 배열로 저장
for _ in range(n):
    coordinate.append(list(map(int, input().split())))
# 람다를 이용해 x를 먼저 오름차순 정렬하고, 동일 값에 대해 y를 기준으로 오름차순 정렬
coordinate.sort(key=lambda x: (x[0], x[1]))

for i in coordinate:
    print(f"{i[0]} {i[1]}")