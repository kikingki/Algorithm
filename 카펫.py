import math

def solution(brown, yellow):
    answer = []
    area = brown + yellow               # 카펫의 넓이
    # 자연수 N의 제곱근까지의 약수를 구하면 그 짝이 되는 약수는 자동으로 구할 수 있음.
    for h in range(3, int(math.sqrt(area))+1):
        if area % h == 0:                # area의 약수 [w*h=area]
            w = area//h
            if w < h:
                break
            # 갈색은 노란색의 테두리 -> (가로-2)*(세로-2) == yellow여야 함.
            if (w-2)*(h-2) == yellow:
                answer = [w,h]
    return answer