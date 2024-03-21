def solution(strArr):
    answer = 0
    a = [len(i) for i in strArr]
    b=[]
    for i in set(a):
        b.append(a.count(i))
        print(b)
    answer = max(b)  
    return answer

a= ["aqg","a","bc","d","efg","hi","sda","sd"]
print(solution(a))