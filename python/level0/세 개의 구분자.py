def solution(myStr):
    answer = []
    myStr = myStr.replace('a',' ')
    myStr =myStr.replace('b',' ')
    myStr =myStr.replace('c',' ')
    myStr = ''.join(myStr)
    myStr = myStr.split()
    
    if myStr == []:
        answer.append('EMPTY')
    else:
        answer.extend(myStr)

    return answer

a = "cabab"
print(solution(a))