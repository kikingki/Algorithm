def checker(w):
    if len(w) == 1:     # 길이가 1이면 무조건 그룹 단어
        return True
    check = []

    for i in range(len(w)):
        if w[i] not in check:
            check.append(w[i])
            continue
        elif w[i-1] == w[i]:    # w[i]가 check에 있을 때 연속되는 문자인지 확인
            check.append(w[i])

    if w != ''.join(check):
        return False
    return True

n = int(input())
group = 0
for _ in range(n):
    word = input()
    if checker(word):
        group += 1
print(group)

'''
문자열 슬라이싱을 이용한 간결한 코드
n = int(input())
group_word = n

for i in range(n):
    word = input()
    for j in range(len(word)-1):
        # 연속해서 나타날 경우 / pass는 실행할 코드가 없음 == 다음 행동을 계속해서 진행
        if word[j] == word[j+1]:        
            pass                        
        # 연속하지 않고, 떨어져서 나타날 경우 그룹 단어가 아니므로 1을 감소하고 반복 종료
        elif word[j] in word[j+1:]:     
            group_word -= 1
            break
print(group_word)
'''