def solution(arr, n):
    answer = []
    for i in range(len(arr)):
        if len(arr) & 1:
            if i & 1:
                answer.append(arr[i])
            else:
                answer.append(arr[i]+n)
        else:
            if i & 1:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
    return answer