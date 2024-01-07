def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(i) 
    return answer

# 만약 저걸 줄이면
# def solution(arr):
#     i = [i for i in arr for j in range(i)]
#     return i