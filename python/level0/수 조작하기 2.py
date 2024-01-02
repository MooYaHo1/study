def solution(numLog):
    answer = ''
    a=1
    for i in numLog[1:]:
        if numLog[a-1]<i:
            if i == (numLog[a-1]+10):        
                answer = answer +('d')
            else:
                answer = answer +('w')
        
        else:
            if i == (numLog[a-1]-10):        
                answer = answer +('a')
            else:
                answer = answer +('s')
        a+=1
    return answer

print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))