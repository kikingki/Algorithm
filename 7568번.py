n = int(input())
person_list = []
rank = [0 for _ in range(n)]

# 튜플 자료형
for _ in range(n):
    h, w = map(int, input().split())
    person_list.append((h, w))

# n명의 인원의 키와 몸무게를 비교하는 모든 경우의 수 - 브루트포스 알고리즘
for i in range(n):
    cnt = 1
    for j in range(n):
        # 키와 몸무게가 모두 커야 자신보다 더 큰 덩치의 사람
        if person_list[i][0] < person_list[j][0] and person_list[i][1] < person_list[j][1]:
            cnt += 1
    rank[i] = cnt

print(" ".join(map(str, rank)))