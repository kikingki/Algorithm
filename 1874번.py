import sys
input = sys.stdin.readline

n = int(input())
count = 1
stack = []
# push, pop 연산 리스트
result = []
# 가능 여부
temp = True

# 반복에서 i를 사용하지 않기 때문에 _로 바꿔줌.
for _ in range(n):
    num = int(input())

    while count <= num:
        # push
        stack.append(count)
        result.append('+')
        count += 1

    # stack의 마지막 값이 num과 동일하면
    if stack[-1] == num:
        # pop
        stack.pop()
        result.append('-')
    # 동일하지 않으면
    else:
        # 입력된 수열 만들기 불가능
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in result:
        print(i)
