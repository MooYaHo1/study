def solution(num_list):
    answer = 0
    a=1
    b=0
    for i in num_list:
        a = a * i
        print('a',a)
        b = b + i
        print(b)
    if a > (b**2):
        answer = 0
    else:
        answer = 1
        
    return answer
a=[5,7,8,3]
print(solution(a))