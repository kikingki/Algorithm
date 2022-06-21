def solution(s):
    len_list = []

    if len(s) == 1:
        return 1

    for i in range(1, (len(s)//2)+1):   # 문자열을 자를 수 있는 최대 단위는 문자열 길이의 절반까지
        temp = s[:i]                    # i 단위로 자른 첫번째 문자열 대입
        cnt = 1                         # 연속되는 값의 개수
        w = ""                          # 압축된 문자열을 담을 변수

        for j in range(i, len(s), i):   # i 단위로 건너뛰기
            if temp == s[j:j+i]:        # 문자가 연속될 경우
                cnt += 1
            else:                       # 연속이 끝날 때 문자열에 삽입
                if cnt > 1:
                    w += str(cnt)+temp
                else:
                    w += temp
                temp = s[j:j+i]         # 다음 문자열 저장, cnt 초기화
                cnt = 1

        # 마지막 문자열 추가
        if cnt > 1:
            w += str(cnt) + temp
        else:
            w += temp
        len_list.append(len(w))
    return min(len_list)