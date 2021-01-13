import sys, math
input = sys.stdin.readline

m, n = map(int, input().split())

board = []
count_list = [] #각 경우의 수마다 바꿔야하는 칸의 수를 모두 종합한 리스트

for _ in range(m):
    board.append(input())

# m*n의 보드판에서 8*8보드가 나오는 모든 경우의 수는 m-7*n-7개
for i in range(m-7):
    for j in range(n-7):
        count_w = 0
        count_b = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                # 행과 열의 인덱스 합이 짝수인지 홀수인지로 체크무늬를 판단할 수 있음
                if (k + l) % 2 == 0:
                    if board[k][l] != "B":
                        count_b += 1
                    else:
                        count_w += 1
                else:
                    if board[k][l] != "W":
                        count_b += 1
                    else:
                        count_w += 1
        count_list.append(count_b)
        count_list.append(count_w)

#가장 최솟값 출력
print(min(count_list))

