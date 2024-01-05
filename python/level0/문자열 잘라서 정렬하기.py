def solution(myString):
    answer = []
    myString = myString.replace('x',' ')
    myString = myString.split()
    print(myString)
    myString.sort()
    answer.extend(myString)
    return answer