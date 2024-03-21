def solution(arr, idx):
    answer = 0
    a = idx
    for i in range(idx,len(arr)):
        if arr[i]==1:
            answer = i
            return answer
    if answer == 0 and idx != 0 :
        answer = -1
    return answer