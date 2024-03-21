def solution(arr, queries):
    answer = []
    q = []
    for a,b,c in queries:
        for i in range(a,b+1):
            if i % c == 0:
                arr[i] += 1

    answer = arr
    return answer

r=[0, 1, 2, 4, 3]
t=[[0, 4, 1],[0, 3, 2],[0, 3, 3]]	
print(solution(r,t))