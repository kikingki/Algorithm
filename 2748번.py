# # 시도1 - 재귀함수는 시간복잡도가 O(2**n)으로 시간이 초과됨.
# def fibonacci_rec(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# 시도2 - 반복문을 사용하면 시간복잡도가 O(n)
def fibonacci_iter(n):
    if n < 2:
        return n
    f1 = 0
    f2 = 1
    for _ in range(n):
        f1, f2 = f2, f1+f2
    return f1

n = int(input())
print(fibonacci_iter(n))
