def solution(n):
    answer = 0
    a = 2
    while n % a != 1:
        a+=1
    answer=a
    return answer