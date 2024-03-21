def solution(num_list):
    answer = 0
    for i in num_list:
        if i > 0:
            answer += 1
    if answer == len(num_list) and num_list[0]>0:
        answer = -1
    return answer