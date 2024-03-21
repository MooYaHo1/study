def solution(arr):
    answer = []
    stk = []
    for i in range(len(arr)):
        if stk == []:
            stk.append(arr[i])
        elif arr[i] == stk[-1]:
            stk.pop()
        else:
            stk.append(arr[i])
    if stk == []:
        stk.append(-1)
    answer = stk
    return answer
a=[0, 1, 1, 1, 0]
print(solution(a))