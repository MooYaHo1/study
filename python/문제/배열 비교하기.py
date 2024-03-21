def solution(arr1, arr2):
    answer = 0
    a=0
    b=0
    if len(arr1) == len(arr2):
        for i in arr1:
            a += i
        for i in arr2:
            b += i
        if a < b:
            answer = -1
        elif a > b:
            answer = 1
        else:
            answer = 0
    else:
        if len(arr1) < len(arr2):
            answer = -1
        elif len(arr1) > len(arr2):
            answer = 1
        else:
            answer = 0
    return answer