def solution(number, k):
    if k == 0:
        return number

    answer = []  # Stack
    for num in number:
        # answer이 비어있지 않고, stack의 마지막 값이 num보다 작고, k>0일 때 pop 반복
        while answer and int(answer[-1]) < int(num) and k > 0:
            print(answer.pop())
            k -= 1
        answer.append(num)

    # k>0이고 반복이 종료됐을 때, ex)number="987653241", k=5->3, answer="9876541", ex)number="999", k=2->2, answer="999"
    answer = answer[:len(answer) - k]
    return ''.join(answer)