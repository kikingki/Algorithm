def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # 중복 제거
    lost_copy = [l for l in lost if l not in reserve]
    reserve_copy = [r for r in reserve if r not in lost]

    for l in reserve_copy:
        if l-1 in lost_copy:
            lost_copy.remove(l-1)
        elif l+1 in lost_copy:
            lost_copy.remove(l+1)

    answer = n - len(lost_copy)
    return answer