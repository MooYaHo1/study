def solution(a, b):
    answer = 0
    if a & 1 and b & 1:
        answer = a**2 + b**2
    elif a &1 ==0 and b &1 ==0:
        answer = abs(a-b)
    else:
        answer = 2 * (a + b)
    return answer