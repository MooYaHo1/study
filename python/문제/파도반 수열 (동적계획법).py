def pado(n):
    p = [0] * 101
    p[1] = 1
    p[2] = 1
    p[3] = 1

    for i in range(4,n+1):
        p[i] = p[i-3] + p[i-2]
    return p[n]

n = int(input()) # 2개의 답을 입력 받을거임
for i in range(n): # 답 순차 입력
    N = int(input())
    print(pado(N))