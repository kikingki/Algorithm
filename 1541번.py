# 식은 양수와 +, -, 그리고 괄호만으로 이루어짐 / 연속해서 2개 이상의 연산자X


num_list = input().split('-')           # -를 기준으로 괄호로 묶을 리스트
sum_list = []

for i in range(len(num_list)):
    plus = 0
    plus_list = num_list[i].split('+')   # +를 기준으로 분할한 리스트
    for n in plus_list:
        plus += int(n)
    sum_list.append(plus)              # plus_list를 정수로 변환해 더한 값의 리스트

result = sum_list[0]
for i in range(1, len(sum_list)):
    result -= sum_list[i]

print(result)

