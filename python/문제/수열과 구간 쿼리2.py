def solution(arr, queries):
    answer = []
    a = []
    for i in queries:
        for j in arr[i[0]:i[1]+1]:
            if j > i[2]:
                a.append(j)
        if a == []:
            a.append(-1)
        answer.append(min(a))
        a = []    
    return answer

q=[0, 1, 2, 4, 3]
w=[[0, 4, 2],[0, 3, 2],[0, 2, 2]]
print(solution(q,w))