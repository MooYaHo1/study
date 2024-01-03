def solution(my_string, s, e):
    answer = ''
    a=[]
    for i in range(s,e+1):
        a.append(my_string[i])
    a.reverse()
    print(a)
    a = ''.join(a)
    answer = my_string[:s] + a + my_string[e+1:]
    return answer

q="Progra21Sremm3"
w=6
e=12
print(solution(q,w,e))

a[::-1]

