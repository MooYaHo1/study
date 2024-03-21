def solution(participant, completion):
    answer = {}
    hash_val = 0
    
    for i in participant:
        answer[hash(i)] = i
        hash_val += hash(i)
    for j in completion:
        hash_val -= hash(j)
    
    return answer[hash_val]