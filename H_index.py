def solution(citations):
    if set(citations) == {0}:
        return 0

    citations.sort(reverse=True)
    h_index = 0

    for idx, val in  enumerate(citations):
        if idx < val:
            h_index = idx+1
    return h_index