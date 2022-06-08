t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h   # 층 수
    room = n//h+1   # 호 수
    if n % h == 0:  # n이 h의 배수일 경우
        floor = h
        room = n//h
    print(str(floor*100+room))
