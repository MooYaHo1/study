def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i] == True:
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop()
    return answer

a=[3, 2, 4, 1, 3]
b=[True, False, True, False, False]
print(solution(a,b))
