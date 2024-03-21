def solution(binomial):
    answer = 0
    a, b, c=binomial.split()
    a, c = int(a), int(c)
    if b == '+':
        answer = a + c
    elif b == '*':
        answer = a * c
    else:
        answer = a - c
    return answer