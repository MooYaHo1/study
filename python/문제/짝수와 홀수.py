def solution(num):
    answer = ''
    if num & 1:
        answer = 'Odd'
    else:
        answer = 'Even'
        
    return answer