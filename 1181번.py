import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

words = list(set(words))    # set 자료형으로 중복 제거
# 먼저 사전순 정렬 후 길이순 정렬을 해야 함.
words.sort()
words.sort(key=len)

print('\n'.join(words))