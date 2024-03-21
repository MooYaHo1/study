def solution(start, end_num):
    answer = []
    for i in range(end_num,start+1):
        answer.append(i)  
    answer.reverse()
    return answer