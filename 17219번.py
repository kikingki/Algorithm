import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}

for i in range(n):
    site, password = input().split()
    dict[site] = password

try:
    for i in range(m):
        print(dict[input().strip()]) # readlines() 혹은 read()함수를 쓰면 \n 값이 같이 읽힘
except KeyError:    #오류 발생시 메시지 출력
    print("저장되지 않은 사이트입니다.")