def solution(arr, k):
    answer = []
    for i in arr:
        if answer == []:
            answer.append(i)
        elif len(answer) < k and i not in answer:
            answer.append(i)
    while len(answer) != k:
        answer.append(-1)
        
    return answer

a=[2, 1, 1, 2, 2, 2]
b=3
print(solution(a,b))