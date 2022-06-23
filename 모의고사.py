def solution(answers):
    answer = [0, 0, 0]
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if student1[i % 5] == answers[i]:
            answer[0] += 1
        if student2[i % 8] == answers[i]:
            answer[1] += 1
        if student3[i % 10] == answers[i]:
            answer[2] += 1

    high_score = []
    for i in range(3):
        if answer[i] >= max(answer):
            high_score.append(i + 1)

    return high_score