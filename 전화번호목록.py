# 방법1 - 이중 for문 사용으로 시간복잡도가 O(n^2)이므로 효율성 테스트 3,4 실패
# def solution(phone_book):
#     n = len(phone_book)
#     for i in range(n-1):
#         for j in range(1,n):
#             if phone_book[i] == phone_book[j]:
#                 continue
#             answer = phone_book[i].startswith(phone_book[j]) or phone_book[j].startswith(phone_book[i])
#             if answer:
#                 return False
#     return True

# 방법2 - 리스트 정렬을 이용하면 근접한 문자열만 검사해주면 됨. 시간복잡도 O(nlogn)
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

# 방법3 - 해시를 사용한 방법. 딕셔너리 자료형은 탐색의 시간 복잡도가 O(1)이다. 이중 for문을 사용했지만 전화번호의 길이가 20자 제한이므로 시간복잡도는 O(n)
def solution(phone_book):
    dict = {}
    for phone_number in phone_book:
        dict[phone_number] = 1
        
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in dict and temp != phone_number:
                return False
    return True