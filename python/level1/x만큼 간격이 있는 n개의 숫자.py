def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x*(i+1))
    return answer

#컴프리핸션
def solution(x, n):
    # 함수를 완성하세요
    return [(i+1) * x for i in range(n)]