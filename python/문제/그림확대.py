def solution(picture, k):
    answer = []
    q = 0
    g=[]
    for i in picture:
        a = []
        for j in range(len(i)):
            b = i[j]*k
            a.append(b)
        a = ''.join(a)
        answer.append(a)
    for i in answer:
        for j in range(k):
            g.append(i)
    
    
    return g
a=[".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]
b=2
print(solution(a,b))