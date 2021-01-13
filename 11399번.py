import sys
input = sys.stdin.readline

p = int(input())
t = list(map(int, input().split()))
time = 0
sum = 0

t.sort()    # 인출시간이 빠른 순서대로 정렬

for i in range(0,len(t)):
    sum += t[i]     #각 사람이 인출하는 데 걸리는 시간
    time += sum      #인출시간의 총합

print(time)