def solution(my_string, m, c):
    answer = ''
    d = ''
    a = 0
    b = []
    for i in my_string:
        if a < m:
            d += i
            a +=1
        else:
            b.append(d)
            d = i
            a = 1
    b.append(d)
    print(b)
    for j in b:
        answer += j[c-1]
    return answer

my_string = "ihrhbakrfpndopljhygc"
m = 4
c = 2

print(solution(my_string, m, c))
