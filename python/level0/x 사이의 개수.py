def solution(myString):
    answer = []
    a = []
    myString = myString.split('x')
    for i in myString:
        if i != '':
            i = len(i)
            answer.append(i)
        else:
            answer.append(0)
    return answer