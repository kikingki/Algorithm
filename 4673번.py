numbers = set(range(1, 10001))
remove_set = set()          # 생성자가 있는 숫자 set

for num in numbers:
    for n in str(num):      # 문자열로 변환해서 각 자릿수끼리 분리 가능
        num += int(n)       # 자릿수끼리 더함. -> 생성자가 있는 숫자
    remove_set.add(num)     # add 함수로 set에 추가

# set 함수의 차집합을 이용해 간단하게 연산 가능
sef_numbers = numbers - remove_set
for self_num in sorted(sef_numbers):
    print(self_num)
