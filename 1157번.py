# # 대소문자를 구분하지 않고 대문자로 출력해야하므로 upper() 사용
# word = input().upper()
# alpha = {}

# # 딕셔너리를 사용해 단어마다 사용 횟수를 셈
# for i in word:
#     if i in alpha:
#         alpha[i] += 1
#     else:
#         alpha[i] = 1

# # 가장 많이 사용된 알파벳 k와 사용횟수 v
# k = ""
# v = 0
# for i in alpha:
#     if alpha[i] > v:    # v보다 value가 크면 갱신
#         v = alpha[i]
#         k = i
#     elif alpha[i] == v:
#         k = "?"
# print(k)


word = input().upper()
# 알파벳 문자열
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cnt_word = []

# 인덱스가 알파벳의 순서이고, 값이 사용 횟수
for i in alpha:
    cnt_word.append(word.count(i))
    
    
# 가장 많이 사용한 알파벳의 사용 횟수와 인덱스
most_value = max(cnt_word)
most_index = cnt_word.index(most_value)

# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우
if cnt_word.count(most_value) > 1:
    print("?")
else:
    print(alpha[most_index])