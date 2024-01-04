def solution(myString, pat):
    # pat으로 시작하는 마지막 인덱스 찾기
    index = myString.rfind(pat)
    if index != -1:
        # 찾은 인덱스부터 끝까지의 부분 문자열 반환
        return myString[:index + len(pat)]
    else:
        return ""

a="AbCdEFG"
b="dE"
print(solution(a,b))