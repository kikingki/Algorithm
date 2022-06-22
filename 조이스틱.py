def solution(name):
    if set(name) == {'A'}:  # A로만 구성될 경우
        return 0

    answer = 0
    move = len(name) - 1  # 오른쪽으로만 이동할 때의 최소 횟수 = 길이 - 1

    for i in range(len(name) - 1, -1, -1):  # 맨 뒤에서 'A'가 연달아 있을 때 이동할 필요X => 이동 횟수-1
        if name[i] == 'A':
            move -= 1
        else:
            break

    for i, alpha in enumerate(name):
        # 알파벳 변경 조작 횟수(상하 조작)
        answer += min(ord(name[i]) - ord("A"), ord("Z") - ord(name[i]) + 1)

        # 커서이동 횟수(좌우 조작)
        next = i + 1  # 현재 위치 i / next는 다음 알파벳의 index
        while next < len(name) and name[next] == 'A':
            next += 1  # 'A'가 아닌 다음 알파벳의 위치
        move = min(move, i * 2 + len(
            name) - next)  # 오른쪽으로 가다가 연속된 A를 만나면 처음으로 돌아가(i*2) + 마지막 위치에서부터 왼쪽으로 가는 값(len(name) - next)
        move = min(move, (len(
            name) - next) * 2 + i)  # 왼쪽으로 가다가 연속된 A를 만나면 마지막으로 돌아가(len(name) - next)*2) + 처음위치에서 오른쪽으로 가는 값(i)
    answer += move

    return answer