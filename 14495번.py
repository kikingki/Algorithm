# # 시도1 - 재귀함수는 시간복잡도가 O(2^n)으로 시간이 초과됨.
# def fibonacci_rec(n):
#     if n < 4:
#         return 1
#     return fibonacci_rec(n-1) + fibonacci_rec(n-3)

# 시도2 - 반복문의 경우 시간복잡도 O(n)
def fibonacci_iter(f, n):
    for i in range(n+1):
        # f(1) = f(2) = f(3) = 1
        if i >= 4:
            f[i] = f[i-1] + f[i-3]

    return f

n = int(input())
f = [1 for _ in range(n+1)]
fibonacci_iter(f, n)
# 리스트의 가장 끝 요소 출력
print(f[-1])