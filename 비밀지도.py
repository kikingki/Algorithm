def solution(n, arr1, arr2):
    answer = []

    # 10진수를 2진수로 변환해서 2차원 리스트로 만듬
    for i in range(n):
        temp = format(arr1[i], 'b')
        binary = "0" * (n - len(temp))
        binary += temp
        arr1[i] = list(binary)
    for i in range(n):
        temp = format(arr2[i], 'b')
        binary = "0" * (n - len(temp))
        binary += temp
        arr2[i] = list(binary)

    for y in range(n):
        str = ""
        for x in range(n):
            if arr1[y][x] == "0" and arr2[y][x] == "0":
                str += " "
            else:
                str += "#"
        answer.append(str)
    return answer