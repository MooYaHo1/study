def solution(my_string, is_suffix):
    answer = 0
    a=[]
    for i in range(len(my_string)):
        a.append(my_string[i:])
    if is_suffix in a:
        answer = 1
    else:
        answer = 0
    return answer
a="banana"
b="nan"
print(solution(a,b))