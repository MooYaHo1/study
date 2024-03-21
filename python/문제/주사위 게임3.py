from collections import Counter
def solution(a, b, c, d):
    answer = 0
    q=[a,b,c,d]
    frequency_list = Counter(q)
    q = sorted(q, key=lambda x: (-frequency_list[x]))

    e=[]
    f=[]
    g=[]
    h=[]
    for i in q:
        if e == []:
            e.append(i)
        elif e[-1] == i:
            e.append(i)
        elif e[-1] != i and f == []:
            f.append(i)
        elif f[-1] == i:
            f.append(i)
        elif f[-1] != i and g == []:
            g.append(i)
        elif g[-1] == i:
            g.append(i)
        else:
            h.append(i)
    if len(e) == 4:
        answer = e[0]*1111
    elif len(e) == 3:
        answer = (10 * e[0] + f[0])**2
    elif len(e) == 2 and len(f) == 2:
        answer = (e[0] + f[0]) * (abs(e[0]-f[0]))
    elif len(e) == 2 and len(f) == 1:
        answer = f[0] * g[0]
    else:
        answer = min(q)
        
    return answer