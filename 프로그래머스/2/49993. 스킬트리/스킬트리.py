def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        idx = 0
        for s in tree:
            if s in skill:
                if skill[idx] != s:
                    break
                if idx + 1 < len(skill):
                    idx += 1
        else:
            answer += 1

    return answer