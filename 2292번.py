n = int(input())
# 한 바퀴의 마지막 방 번호
end = 1
# 지나가는 방의 개수
room = 1

while n > end:
    # 벌집이 6의 배수로 증가
    end += 6 * room
    room += 1
print(room)



