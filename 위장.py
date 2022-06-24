def solution(clothes):
    answer = 1
    dic = {}

    # 변수를 n개 지정하면 2차원 배열의 요소인 1차원 리스트에서 요소 n개를 꺼낸다. 1차원 배열 요소⊂1차원 배열⊂2차원 배열
    for _, category in clothes:
        if dic.get(category):           # 옷의 종류별 개수
            dic[category] += 1
        else:
            dic[category] = 1
    # dic = Counter([category for name, category in clothes]) -> Counter 함수 사용

    # 경우의 수 계산 공식, 해당 종류의 옷의 개수에 +1을 하는 이유는 그 종류의 옷을 안입는 경우도 포함
    for k, v in dic.items():
        answer *= v+1
    # 하지만, 하루에 최소 한 개의 의상은 입어야 하므로 아무것도 입지 않은 경우는 제외
    answer -= 1
    return answer