def solution(my_string):
    answer = [0 for i in range(52)]
    for c in my_string:
        if ord(c) > ord('Z'):
            answer[ord(c)-ord('a')+26] += 1
        else:
            answer[ord(c)-ord('A')] += 1
    return answer
print(solution('result'))

# ord가 아스키코드 숫자 출력 A = 65  a =80