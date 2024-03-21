def solution(arr, query):
    answer = []
    for i in range(len(query)):
        print(i)
        if i % 2 == 0:
            arr = arr[:query[i]+1]

        else:
            arr = arr[query[i]:]

    answer = arr
    return answer

a=[0, 1, 2, 3, 4, 5]
b=[4, 1, 2]
print(solution(a,b))