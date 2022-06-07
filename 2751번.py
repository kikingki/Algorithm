'''
범위가 1 ≤ N ≤ 1,000,000이므로 시간복잡도가 중요한 문제 >> 시간복잡도가 O(nlogn)인 merge sort 이용
merge sort는 분할 정복 방식을 사용하여, 보통 재귀 함수를 이용해서 구현
'''
# 입력값이 많을 경우 readline을 사용하면 좋음
import sys
input = sys.stdin.readline

def merge(li):
    if len(li) <= 1:    # 리스트의 요소가 1이면 정렬X
        return

    mid = len(li) // 2  # 중간값을 기준으로 분할
    g1 = li[:mid]
    g2 = li[mid:]
    # 재귀 호출
    merge(g1)
    merge(g2)

    # g1, g2 병합
    i1 = 0      # g1의 인덱스
    i2 = 0      # g2의 인덱스
    li_idx = 0     # li의 인덱스

    while i1 < len(g1) and i2 < len(g2):
        # 더 작은 값을 li에 추가 후 li의 인덱스 1 증가
        if g1[i1] < g2[i2]:
            li[li_idx] = g1[i1]
            i1 += 1
        else:
            li[li_idx] = g2[i2]
            i2 += 1
        li_idx += 1

    # while문이 끝나고 남은 데이터는 리스트에 정렬되어 들어간 값보다 크다. 즉, 값을 비교할 필요가 없다.
    while i1 < len(g1):
        li[li_idx] = g1[i1]
        i1 += 1
        li_idx += 1
    while i2 < len(g2):
        li[li_idx] = g2[i2]
        i2 += 1
        li_idx += 1

# 입력값 저장
n = int(input())
num_li = [0] * n
for i in range(n):
    num_li[i] = int(input())

merge(num_li)

# 문자열 변수를 만들어서 출력 - 시간↓ 메모리↑
s = ""
for i in num_li:
    s += (str(i)+'\n')
print(s)
