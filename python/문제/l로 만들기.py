def solution(myString):
    answer = []
    for i in myString:
        if ord(i) < ord('l'):
            answer.append('l')
        else:
            answer.append(i)
    answer = ''.join(answer)
    return answer