def solution(arr):
    answer = []
    a=0
    for i in range(0,11):
        a= 2 ** i
        while len(arr) < a: 
            arr.append(0)
        if len(arr) == a:
            break
    answer = arr
    return answer
arr=[1]
print(solution(arr))