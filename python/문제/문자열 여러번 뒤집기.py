# def solution(my_string, queries):
#     answer = ''
#     my_string = list(my_string)
#     for i in queries:
#         my_string[i[0]], my_string[i[1]] = my_string[i[1]],my_string[i[0]]
#         print(my_string)
#     answer = ''.join(my_string)    
#     return answer

def solution(my_string, queries):
    answer = ''
    e = []
    my_string = list(my_string)
    for i in queries:
        for j in range(i[0], i[1]+1):
            e.append(my_string[j])
        e.reverse()
        print('예시1',my_string[0:i[0]])
        print('예시2',e)
        print('예시3',my_string[i[1]+1:-1])
        my_string = (my_string[0:i[0]] + e + my_string[i[1]+1:])
        print('예시4',my_string)
        e=[]
        
    answer = ''.join(my_string)

    return answer

q = "rermgorpsam" 
w = [[2, 3], [0, 7], [5, 9], [6, 10]]
print(solution(q, w))