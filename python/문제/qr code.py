def solution(q, r, code):
    answer = ''
    code = list(code)
    a = []
    for i in range(len(code)):
        if i % q == r:
            a.append(code[i])
    answer = ''.join(a)
    return answer
a = 3
b =1
c = "qjnwezgrpirldywt"
print(solution(a,b,c))