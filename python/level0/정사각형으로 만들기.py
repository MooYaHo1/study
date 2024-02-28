def solution(arr):
    answer = [[]]
    if len(arr) > len(arr[0]):
        a=len(arr)-len(arr[0])
        for i in range(len(arr)):
            for j in range(a):
                arr[i].append(0)
    elif len(arr) < len(arr[0]):
        b=len(arr[0])-len(arr)
        for q in range(b):
            arr.append([0]*len(arr[0]))       
    return arr