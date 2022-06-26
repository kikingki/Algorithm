def solution(numbers, target):
    answer = 0

    def dfs(target, n, result):
        nonlocal answer  # 중첩된 함수에서 밖에 있는 비지역 변수를 사용
        if n == len(numbers):  # 연산 횟수가 numbers의 개수일 때 결과가 타겟 넘버인지 확인
            if target == result:
                answer += 1
            return
        else:  # numbers[n]의 각 숫자들을 더하거나 빼는 경우를 동시에 가지처럼 확장
            dfs(target, n + 1, result + numbers[n])
            dfs(target, n + 1, result - numbers[n])

    dfs(target, 0, 0)
    return answer