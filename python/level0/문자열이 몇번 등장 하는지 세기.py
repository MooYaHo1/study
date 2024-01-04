def solution(myString, pat):
    answer = 0
    while pat in myString:
            index = myString.find(pat)
            if pat in myString:
                myString = myString[index+1:]
                answer +=1
    return answer

a = 'abab'
b = 'aa'
print(solution(a,b))