def solution(arr):
    answer = []
    a = []
    b = 0
    for i in range(len(arr)):
        if arr[i] == 2:
            a.append(i)
            b += 1
    if b >= 1:
        answer = arr[a[0]:a[-1]+1]
    else:
        answer.append(-1)
    return answer