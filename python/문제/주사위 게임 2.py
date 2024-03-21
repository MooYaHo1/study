def solution(a, b, c):
    answer = 0
    i = a + b + c
    o = a**2 + b**2 + c**2
    p = a**3 + b**3 + c**3
    if a != b and a != c and b != c:
        answer = i
    elif a == b and a == c and b == c:
        answer = i * o * p
    else:
        answer = i * o
        
    return answer

print(solution(5, 3, 3))