def solution(board, moves):
    answer = 0
    bucket = []

    for x in moves:
        for y in range(len(board)):
            if board[y][x - 1]:
                bucket.append(board[y][x - 1])
                board[y][x - 1] = 0
                break
        if len(bucket) >= 2 and bucket[-2] == bucket[-1]:
            bucket.pop()
            bucket.pop()
            answer += 2
    return answer