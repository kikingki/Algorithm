from itertools import permutations
import math

# 시도1 - 에라토스테네스의 체 사용(문자열이 길면 2000ms 가까이 나옴)
"""
def solution(numbers):
    num_list = list(numbers)                    # 문자열을 한 글자씩 분리
    per_list = []                               # 조합할 수 있는 모든 경우의 수 리스트(수의 순서가 상관있으므로 순열)

    for i in range(1, len(num_list) + 1):       # 1~num_list의 길이만큼 수 조합을 만듬.
        for j in permutations(num_list, i):
            per_list.append(int(''.join(j)))
    per_list = sorted(set(per_list))            # 중복 제거 후 정렬
    answer = 0

    m = int(len(numbers) * "9")                 # 에라토스테네스의 체의 범위(numbers의 최대 자릿수만큼)

    def eratos(m):                              # 시간복잡도 - O(NloglogN)
        sieve = [True] * m
        sieve[0] = False
        sieve[1] = False

        s = int(math.sqrt(m))

        for i in range(2, s + 1):
            if sieve[i] == True:                # i가 소수이면 i의 배수들은 합성수이므로 False로 바꿈(점점 제외할 값이 줄어듬-속도↑)
                for j in range(i * i, m, i):
                    sieve[j] = False
        return sieve

    p_li = eratos(m)                            # 소수 리스트 (True인 값의 index가 소수)

    for i in range(len(p_li)):
        if p_li[i] and i in per_list:
            answer += 1
    return answer
"""

# 시도2 - 경우의 수 리스트에서 소수 판별(최대가 약 6ms)
def solution(numbers):
    num_list = list(numbers)  # 문자열을 한 글자씩 분리
    per_list = []  # 조합할 수 있는 모든 경우의 수 리스트(수의 순서가 상관있으므로 순열)

    for i in range(1, len(num_list) + 1):  # 1~num_list의 길이만큼 수 조합을 만듬.
        for j in permutations(num_list, i):
            per_list.append(int(''.join(j)))

    per_list = sorted(set(per_list))  # 중복 제거 후 정렬
    answer = 0

    def chk_prime(number):  # 소수 판별
        if number < 2:
            return False
        # 합성수 n이 p x q로 표현될 때 적어도 하나는 √n 값의 이하라는 점을 이용
        # ex) n=80, √n=8.xxx -> 1*80, 2*40, 4*20, 5*16, 8*10
        s = int(math.sqrt(number))
        for i in range(2, s + 1):
            if number % i == 0:
                return False
        return True

    for num in per_list:
        if chk_prime(num):
            answer += 1
    return answer
