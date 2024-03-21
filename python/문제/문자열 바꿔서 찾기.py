def solution(myString, pat):
    answer = 0
    a = []
    for i in myString:
        if i =='A':
            a.append('B')
            print('1', a)
        else:
            a.append('A')
            print('2', a)
    a = ''.join(a)
    if pat in a:
        answer = 1
    else:
        answer = 0
    return answer