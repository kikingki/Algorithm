# n = input()

# # n이 10 이하일 경우 십의 자리에 0 추가
# if int(n) < 10:
#     n = "0"+n

# # 초기값 저장
# m = n

# cycle = 0   # 사이클 변수
# new_num = ''

# while(True):
#     # 사이클이 한번 이상 돌고, 초기값과 새로운 수가 같은 경우 반복 종료
#     if cycle > 0:
#         if n == m:
#             break
#     new_num = str(int(n[0:1])+int(n[1:2]))
#     # 새로운 수가 10 이하이면 위와 동일하게 십의 자리에 0 추가
#     if int(new_num) < 10:
#         new_num = "0"+new_num
#     # 슬라이싱을 이용해 주어진 수의 일의 자리 수와 새로운 수의 일의 자리 수를 이어 붙임
#     n = n[1:2] + new_num[1:2]

#     cycle += 1
# print(cycle)

num = check = int(input())   # check 변수에 초기값 저장
cycle = 0

while(True):
    temp = num//10 + num % 10   # //는 몫(십의 자리), %는 나머지(일의 자리)
    new_num = (num%10)*10 + temp % 10   #num의 일의 자리 수를 십의자리로 바꾸고, temp의 일의 자리 수를 더함
    num = new_num
    cycle += 1

    if new_num == check:
        break

print(cycle)

