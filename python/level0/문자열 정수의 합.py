def solution(num_str):
    answer = 0
    num_str =list(num_str)
    for i in num_str:
        answer += int(i)
    
    return answer