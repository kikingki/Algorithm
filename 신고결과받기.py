def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]   # 유저별 메일 발송 횟수
    report = set(report)                  # 중복 제거
    repo_dict = {x: 0 for x in id_list}         # 신고된 id:신고 횟수

    # 신고된 횟수 계산
    for i in report:
        id, repo = i.split()
        repo_dict[repo] += 1

    # k번 이상 신고되면 해당 유저를 신고한 유저의 메일 발송 횟수 +1
    for i in report:
        id, repo = i.split()
        if repo_dict[repo] >= k:
            answer[id_list.index(id)] += 1
    return answer