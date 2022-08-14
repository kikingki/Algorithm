# 완전 탐색
def solution(prices):
    answer = [0 for _ in range(len(prices))]

    for i in range(len(prices) - 1):
        time = len(prices) - i - 1
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                time = j - i
                break
        answer[i] = time
    return answer


# 스택
'''
현재 시간 시점의 주식 가격이 떨어지지 않고 몇 초를 버텼는지 구하는 문제 
-> 최소:0 ~ 최대:len(prices)-1초
'''
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    
    for i in range(len(prices)):        # i == 현재 시간 시점
        while stack and prices[i] < prices[stack[-1]]:
            # ex) 3초 시점의 가격이 현재 i초의 가격보다 높았으면 3초 시점의 가격이 떨어지지 않은 시간은 i초-3초
            idx = stack.pop()          # i초의 가격보다 가격이 높을 때의 시점
            answer[idx] = i-idx        # idx 시점의 유지 시간
            
            print(f"answer[{idx}] = {i-idx}")
        stack.append(i)
        print(stack)
    
    # 끝까지 가격이 떨어지지 않았을 때
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - 1 - idx
    return answer