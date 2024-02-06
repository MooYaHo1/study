def solution(rank, attendance):
    answer = 0
    a={}
    c=[]
    q=0
    w=0
    e=0
    for i in range(len(rank)):
        if attendance[i] == True:
            a[rank[i]]=attendance[i]
    b=a.keys()
    for i in b:
        c.append(i)
    c.sort()
    for i in range(len(rank)):
        if rank[i] == c[0]:
            q=i
        elif rank[i] == c[1]:
            w=i
        elif rank[i] == c[2]:
            e=i
    answer = 10000*q+100*w+e
    return answer