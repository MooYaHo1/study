def solution(arr, queries):
    answer = []
    c = []
    for a, b in queries:
        c.extend(range(a,b+1))

        for i in c:
            arr[i] += 1
        c = []
    answer = arr
    return answer

arr = [0, 1, 2, 3, 4]
qu = [[0, 1],[1, 2],[2, 3]]
print(solution(arr, qu))