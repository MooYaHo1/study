def solution(intStrs, k, s, l):
    answer = []
    a=0
    for i in intStrs:
        a = int(i[s:s+l])
        if k < a:
            answer.append(a)
    return answer