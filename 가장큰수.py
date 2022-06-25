def solution(numbers):
    if set(numbers) == {0}:
        return "0"
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3)
    numbers.reverse()
    answer = ''.join(numbers)
    return answer