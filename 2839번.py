n = int(input())
b = 0

# Nkg의 설탕을 정확히, 또 최소한의 봉지로 나눠야 한다.

# 5kg의 배수로 딱 나뉘어 떨어질 때까지 설탕의 무게를 3kg씩 빼고 봉지의 개수를 1씩 더한다.
while(True):
    if n % 5 == 0:
        b += n//5
        print(b)
        break
    n = n-3
    b += 1
    # 설탕의 무게가 음수가 되면 정확하게 나누어지지 않는 것이므로 -1을 출력한다.
    if n < 0:
        print(-1)
        break