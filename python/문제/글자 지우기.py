def solution(my_string, indices):
    answer = ''
    my_string = list(my_string)
    a = 0
    indices.sort()
    for i in indices:
        if i != 0:
            del my_string[i-a]
            a+=1
        else:
            del my_string[i]
            a+=1
    answer = ''.join(my_string)
    return answer
a ="apporoograpemmemprs"
b = [1, 16, 6, 15, 0, 10, 11, 3]
print(solution(a,b))