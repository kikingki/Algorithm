# 과목 수 n, 시험 점수 scores, 최고점 m
n = int(input())
scores = list(map(int, input().split()))
m = max(scores)

# 새로 계산한 점수
for i in range(0, len(scores)):
    scores[i] = scores[i]/m*100

print(sum(scores)/n)