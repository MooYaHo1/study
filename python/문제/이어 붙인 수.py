def solution(num_list):
    answer = 0
    a = ''
    b = ''
    for i in num_list:
        if i % 2 == 0:
            a= a+str(i)
        else:
            b= b+str(i)
    answer = int(a) + int(b)
    return answer

a=[3,4,5,2,1]
print(solution(a))