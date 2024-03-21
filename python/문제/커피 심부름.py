def solution(order):
    answer = 0
    a=0
    b=0
    for i in order:
        if 'latte' in i:
            a += 1
        else:
            b += 1
    answer = a * 5000 + b *4500
    return answer