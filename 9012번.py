import sys
input = sys.stdin.readline

# 입력 데이터 수 t
t = int(input())
# 문자열를 입력받을 리스트 ps, VPS를 판별하기 위한 stack
ps = []
stack = []

# 입력
for i in range(t):
    ps.append(input())

for i in ps:
    for j in i:
        # 왼쪽 괄호는 스택에 push
        if j == '(':
            stack.append(j)
        # 오른쪽 괄호는 pop 수행
        elif j == ')':
            # 짝을 맞출 왼쪽 괄호가 없으면 stack에 추가한 후 반복 종료
            if not stack:
                stack.append(j)
                break
            else:
                stack.pop()
    # 반복을 끝내고 stack이 empty 상태면 VPS, 아니면 VPS가 아닌 문자열
    if stack:
        print("NO")
    if not stack:
        print("YES")
    stack = []      # 스택 초기화