def solution(array, commands):
    answer = []
    for i, j, k in commands:
        slice_list = array[i-1:j]
        slice_list.sort()
        answer.append(slice_list[k-1])
    return answer