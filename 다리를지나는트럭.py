from collections import deque

'''
truck_weights[0]의 요소를 꺼내면 O(n) -> truck_weights.reverse()을 해서 끝에서 요소를 pop()하면 O(1)
sum()을 사용하면 매번 queue의 모든 요소를 더하므로 시간이 많이 소요됨. -> 현재 다리 위의 무게 변수를 따로 만들어 처리하면 시간 대폭 축소
'''

def solution(bridge_length, weight, truck_weights):
    answer = 0  # 경과 시간
    bridge = deque(0 for _ in range(bridge_length))  # 다리의 길이만큼 0으로 초기화
    truck_weights.reverse()
    now_weight = 0  # 현재 다리 위의 무게

    while truck_weights:  # truck_weights의 길이가 0이 될 때까지 반복
        answer += 1  # 1초에 1씩 이동
        temp = bridge.popleft()  # 다리를 끝까지 지나가서 제거
        if temp != 0:
            now_weight -= temp
        if now_weight + truck_weights[-1] <= weight:  # now_weight과 다음 트럭의 무게의 합이 weight보다 적으면
            truck = truck_weights.pop()  # truck_weights에서 꺼내서 다리 위에 진입함
            bridge.append(truck)
            now_weight += truck  # 트럭 무게 추가
        else:
            bridge.append(0)  # 0을 추가해 다리 길이를 유지해야 함.
    answer += bridge_length  # 마지막 트럭이 다리를 건너는 시간 추가
    return answer