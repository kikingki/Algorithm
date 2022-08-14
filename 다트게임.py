def solution(dartResult):
    stack = []              # 스택 사용
    dartResult = dartResult.replace("10", "A")  # '10'만 2글자이므로 16진수로 대체
    bonus = {'S': 1, 'D': 2, 'T': 3}

    for i in range(len(dartResult)):
        temp = dartResult[i]
        if temp.isdigit() or temp == 'A':  # 숫자
            stack.append(10 if temp == 'A' else int(temp))
            continue
        elif temp in bonus.keys():  # 보너스
            s = stack.pop()
            stack.append(s ** bonus.get(temp))
        elif temp == '#':  # 해당 점수 -
            s = stack.pop()
            stack.append(-s)
        else:  # 해당 점수와 바로 전에 얻는 점수를 각 2배
            s1 = stack.pop()
            if len(stack):
                s2 = stack.pop()
                stack.append(s2 * 2)
            stack.append(s1 * 2)
    return sum(stack)