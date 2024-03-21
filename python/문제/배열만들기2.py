def solution(l, r):
    answer = []
    a=''
    for i in range(l,r+1):
        if i % 5 == 0:
            a = str(i)
            a=a.replace('0', '')
            a=a.replace('5', '')
            if a == '':
                answer.append(i)
                
                
    if answer == []:
        answer.append(-1)
    return answer

print(solution(5,555))