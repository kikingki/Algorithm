t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a+b}")        # f-string 사용 (문자열 안에 변수 값 삽입)