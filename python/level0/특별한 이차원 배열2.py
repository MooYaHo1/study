def solution(arr):
    answer = 0
    a = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != arr[j][i]:
                a += 1
    if a >= 1:
        answer = 0
    else:
        answer = 1
    return answer # 이게 내가 푼 코드

def solution(arr):
    answer = 0
    a = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1 # 이게 보다 간단한 코드



