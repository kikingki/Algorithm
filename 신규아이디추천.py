import re

def solution(new_id):
    new_id = new_id.lower()                         # step 1
    new_id = re.sub(r"[^a-z-_.0-9]", "", new_id)    # step 2 (^==not, r==문자 그대로 판단)
    new_id = re.sub(r"[.]{2,}", ".", new_id)        # step 3 ({m,n}==m이상 n이하)
    new_id = new_id.strip(".")                      # step 4
    # step 5
    if new_id == "":
        new_id = "a"
    # step 6
    if len(new_id) > 15:
        new_id = new_id[:15].strip(".")
    # step 7
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id