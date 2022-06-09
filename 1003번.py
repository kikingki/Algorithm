def fibonacci(n):
    # zero의 길이를 기준으로 하여 다음 테스트케이스에서 중복되는 연산 생략
    # l = len(zero)
    if n >= 3:
        for i in range(3, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(str(zero[n]) + " " + str(one[n]))

t = int(input())
for _ in range(t):
    n = int(input())
    # n=0일 때, zero 1번, one 0번 호출
    # n=1일 때, zero 0번, one 1번 호출
    # n=2일 때, zero 1번, one 1번 호출
    zero = [1, 0, 1]
    one = [0, 1, 1]
    fibonacci(n)







