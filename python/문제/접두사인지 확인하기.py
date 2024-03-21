def solution(my_string, is_prefix):
    answer = 0
    b=[]
    for i in range(len(my_string)):
        b.append(my_string[:i])
    if is_prefix in b:
        answer = 1
    else:
        answer = 0
    return answer