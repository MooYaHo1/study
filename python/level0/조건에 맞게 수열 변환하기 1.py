def solution(arr):
    answer = []
    for i in arr:
        if i & 1 and i <= 50:
            i *= 2
            answer.append(i)
        elif i % 2 == 0 and i >= 50:
            i /= 2
            answer.append(i)
        else:
            answer.append(i)
            
    return answer